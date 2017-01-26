For instance, I want these to run in the order they appear in the file.

    import unittest

    class MyTests(unittest.TestCase):

        def test_run_me_first(self):
            pass

        def test_2nd_run_me(self):
            pass

        def test_and_me_last(self):
            pass

    if __name__ == "__main
        unittest.main()

Running this gives

    test_2nd_run_me (__main__.MyTests) ... ok
    test_and_me_last (__main__.MyTests) ... ok
    test_run_me_first (__main__.MyTests) ... ok

Not what I want.

The answers I've found here on SO after searching all either say

* "don't do it, just write your tests differently" or

* "name your tests lexicographically!"

Except for [one](http://stackoverflow.com/a/18499093/4532996), which does what I want, but only for one TestCase class. I want to run all my TestCase classes, and I'd like to be able to specify the exact algorithm to use for sorting.

Can I do this in `unittest`?