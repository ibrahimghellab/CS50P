from twttr import shorten
import pytest

def test_default():
    assert(shorten("twitter")=="twttr")
    assert(shorten("aerius")=="rs")
def test_without_vowels():
    assert(shorten("crypt")=="crypt")
    assert(shorten("flyby")=="flyby")
def test_with_only_vowels():
    assert(shorten("ouea")=="")
    assert(shorten("aeiou")=="")
def test_with_number():
    assert(shorten("91390")=="91390")
def test_with_punctuation():
    assert(shorten("hello!")=="hll!")
def test_with_capitalize_letters():
    assert(shorten("HELLO")=="HLL")
