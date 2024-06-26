import unittest
import tempfile
class TestIndexing(unittest.TestCase):

    def test_indexing_1doc(self):
        from pyterrier_colbert.indexing import ColBERTIndexer
        checkpoint="http://www.dcs.gla.ac.uk/~craigm/colbert.dnn.zip"
        import os
        indexer = ColBERTIndexer(
            checkpoint, 
            os.path.dirname(self.test_dir),os.path.basename(self.test_dir), 
            chunksize=3,
            gpu=False)

        indexer.index({
            "docno" : "d1",
            "text": " professor proton mixed the chemicals"
        })

        factory = indexer.ranking_factory()


    def setUp(self):
        import pyterrier as pt
        if not pt.started():
            pt.init()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        try:
            shutil.rmtree(self.test_dir)
        except:
            pass