import os
import khmer

thisdir = os.path.dirname(__file__)
thisdir = os.path.abspath(thisdir)

reads_filename = os.path.join(thisdir, 'test-reads.fa')
N_READS = 25000

class GoodException(Exception):
    pass

def callback_raise(info, n_reads, other):
    raise GoodException

def test_raise_in_consume_fasta_build_readmask():
    kh = khmer.new_hashtable(4, 4**4)

    try:
        kh.consume_fasta_build_readmask(reads_filename, 0, 0, callback_raise)
    except GoodException:
        pass
    except:
        assert 0

def test_raise_in_readmask_filter_fasta_file():
    readmask = khmer.new_readmask(N_READS)

    try:
        readmask.filter_fasta_file(reads_filename, "/dev/null", callback_raise)
    except GoodException:
        pass
    except:
        assert 0

def test_raise_in_fasta_file_to_minmax():
    ht = khmer.new_hashtable(4, 4**4)

    try:
        ht.fasta_file_to_minmax(reads_filename, N_READS, None, callback_raise)
    except GoodException:
        pass
    except:
        assert 0

def test_raise_in_filter_fasta_file_max():
    ht = khmer.new_hashtable(4, 4**4)
    mmt = ht.fasta_file_to_minmax(reads_filename, N_READS)

    try:
        ht.filter_fasta_file_max(reads_filename, mmt, 2, None, callback_raise)
    except GoodException:
        pass
    except:
        assert 0