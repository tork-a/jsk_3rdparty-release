#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

from cStringIO import StringIO
import os
import re
import rospkg
import rospy
import subprocess
import tempfile
from speech_recognition_msgs.msg import Grammar
from speech_recognition_msgs.msg import PhraseRule
from speech_recognition_msgs.msg import Vocabulary


_REGEX_HIRAGANA = re.compile(r'^(?:\xE3\x81[\x81-\xBF]|\xE3\x82[\x80-\x93])+$')


def is_hiragana(s):
    return _REGEX_HIRAGANA.search(s) is not None


def readlines_with_utf8(path):
    assert os.path.exists(path)
    return subprocess.check_output(["nkf", "-w", path]).split(os.linesep)


def load_grammar(path, name):
    assert os.path.isdir(path)
    g = Grammar()
    grammar_path = os.path.join(path, "%s.grammar" % name)
    for l in readlines_with_utf8(grammar_path):
            l = l.strip()
            if l:
                sym, defi = l.strip().split(':')
                r = PhraseRule()
                r.symbol = sym.strip()
                r.definition = [d.strip() for d in defi.split()]
                g.rules.append(r)
    voca_path = os.path.join(path, "%s.voca" % name)
    voca = None
    for l in readlines_with_utf8(voca_path):
        l = l.strip()
        if l.startswith('%'):
            g.categories.append(l[1:].strip())
            if voca:
                g.vocabularies.append(voca)
            voca = Vocabulary()
        elif l:
            sp = l.strip().split()
            voca.words.append(sp[0])
            voca.phonemes.append(' '.join(sp[1:]))
    if voca:
        g.vocabularies.append(voca)
    return g


def make_phonemes_from_words(words):
    cmd = ["rosrun", "julius", "yomi2voca.pl"]
    stdin = os.linesep.join(["%s %s" % (w, w) for w in words]) + os.linesep
    rospy.logdebug("Executing %s" % cmd)
    p = subprocess.Popen(["rosrun", "julius", "yomi2voca.pl"],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result, error = p.communicate(unicode(stdin, 'utf-8').encode('euc-jp'))
    rospy.logdebug("STDOUT: %s" % result)
    rospy.logdebug("STDERR: %s" % error)

    if error and "Error:" in error:
        error = unicode(error, 'euc-jp').encode('utf-8')
        rospy.logerr("Error: %s" % error)
        return None

    result = unicode(result, 'euc-jp').encode('utf-8')
    result = result.split(os.linesep)[:-1]
    result = [r.split("\t")[1] for r in result]

    return result


def make_grammar_from_rules(rules):
    ss = StringIO()
    for r in rules:
        ss.write("{symbol}: {definition}{linesep}".format(
            symbol=r.symbol,
            definition=" ".join(r.definition),
            linesep=os.linesep))
    return ss.getvalue()


def make_voca_from_categories(cats, vocas):
    ss = StringIO()
    for c, vs in zip(cats, vocas):
        ss.write("% {category}{linesep}".format(
            category=c,
            linesep=os.linesep))
        phonemes = vs.phonemes
        if len(phonemes) == 0:
            phonemes = make_phonemes_from_words(vs.words)
        for w, p in zip(vs.words, phonemes):
            ss.write("{word}\t{phoneme}{linesep}{linesep}".format(
                word=w,
                phoneme=p,
                linesep=os.linesep))
    return ss.getvalue()


def make_dfa(grammar, voca):
    name = "data"
    temp_dir = tempfile.mkdtemp(prefix="mkdfa")
    rospy.logdebug("created temp dir: %s" % temp_dir)
    with open(os.path.join(temp_dir, "{name}.grammar".format(name=name)), "w") as f:
        f.write(grammar)
    with open(os.path.join(temp_dir, "{name}.voca".format(name=name)), "w") as f:
        f.write(voca)

    cmd = ["rosrun", "julius", "mkdfa.pl", name]
    rospy.logdebug("Executing %s" % cmd)
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         cwd=temp_dir)
    result, error = p.communicate(temp_dir)
    rospy.logdebug("STDOUT: %s" % result)
    rospy.logdebug("STDERR: %s" % error)

    if "generated:" not in result:
        rospy.logerr("Failed to compile grammar to DFA: %s" % error.strip())
        return None

    with open(os.path.join(temp_dir, "{name}.dfa".format(name=name)), "r") as f:
        dfa = f.read()
    with open(os.path.join(temp_dir, "{name}.dict".format(name=name)), "r") as f:
        dic = f.read()
    return dfa, dic


if __name__ == '__main__':
    result = make_phonemes_from_words(["うどん", "そば"])
    assert result[0] == "u d o N"
    assert result[1] == "s o b a"
