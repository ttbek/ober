'''
============================================================
Test the GERMLINE algorithm for finding IBD segments in a
family with a small # of sibs (4) and two genotyped parent.

Created on September 14, 2012
@author: Oren Livne <livne@uchicago.edu>
============================================================
'''
import unittest, numpy as np, impute as im
from numpy.ma.testutils import assert_equal
from impute import impute_test_util as itu
from impute.ibd import ibd_germline as ig
from impute.tools.param import PhaseParam
from impute.impute_test_util import assert_segments_almost_equal

class TestIbdGermline2Small(unittest.TestCase):
    #---------------------------------------------
    # Constants
    #---------------------------------------------
    
    #---------------------------------------------
    # Setup Methods
    #---------------------------------------------

    def setUp(self):
        '''Load single nuclear family test case.'''
        self.problem = im.io.read_npz(itu.FAMILY4_STAGE3)
        self.family = self.problem.first_family
        self.sibs = ig._filled_members(self.problem, self.family) 
        self.ibd_computer = ig.GermlineIbdComputer(PhaseParam())
    
    #---------------------------------------------
    # Test Methods
    #---------------------------------------------
    def test_ibd_segments(self):
        '''Test computing GERMLINE IBD segments.'''
        m = self.ibd_computer.ibd_segments(ig._HapMatrix(self.problem, self.sibs)).group_to_disjoint()
        assert_segments_almost_equal(m,
                                     [((0   , 20), (16484792, 17318333, 0.834, 0), ((3, 1), (4, 1), (1, 1), (2, 1))),
                                      ((0   , 20), (16484792, 17318333, 0.834, 0), ((0, 1), (3, 0), (5, 0))),
                                      ((0   , 20), (16484792, 17318333, 0.834, 0), ((2, 0), (0, 0), (4, 0))),
                                      ((0   , 20), (16484792, 17318333, 0.834, 0), ((5, 1), (1, 0))),
                                      ((20  , 121), (17318333, 18235305, 0.917, 0), ((5, 1), (4, 1), (1, 1), (2, 1))),
                                      ((20  , 121), (17318333, 18235305, 0.917, 0), ((0, 1), (3, 0), (5, 0))),
                                      ((20  , 121), (17318333, 18235305, 0.917, 0), ((2, 0), (0, 0), (4, 0))),
                                      ((121 , 224), (18235305, 19455836, 1.221, 0), ((5, 1), (4, 1), (1, 1), (2, 1))),
                                      ((121 , 224), (18235305, 19455836, 1.221, 0), ((0, 1), (3, 0), (5, 0))),
                                      ((121 , 224), (18235305, 19455836, 1.221, 0), ((0, 0), (4, 0))),
                                      ((121 , 224), (18235305, 19455836, 1.221, 0), ((1, 0), (3, 1))),
                                      ((224 , 828), (19455836, 27236071, 7.780, 0), ((0, 1), (3, 0), (5, 0), (2, 0))),
                                      ((224 , 828), (19455836, 27236071, 7.780, 0), ((5, 1), (4, 1), (1, 1), (2, 1))),
                                      ((224 , 828), (19455836, 27236071, 7.780, 0), ((0, 0), (4, 0))),
                                      ((224 , 828), (19455836, 27236071, 7.780, 0), ((1, 0), (3, 1))),
                                      ((828 , 2039), (27236071, 37707962, 10.472, 0), ((0, 1), (3, 0), (5, 0), (2, 0))),
                                      ((828 , 2039), (27236071, 37707962, 10.472, 0), ((1, 0), (3, 1), (4, 1))),
                                      ((828 , 2039), (27236071, 37707962, 10.472, 0), ((5, 1), (1, 1), (2, 1))),
                                      ((828 , 2039), (27236071, 37707962, 10.472, 0), ((0, 0), (4, 0))),
                                      ((2039, 2442), (37707962, 44264502, 6.557, 0), ((0, 1), (3, 0), (5, 0), (2, 0))),
                                      ((2039, 2442), (37707962, 44264502, 6.557, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2039, 2442), (37707962, 44264502, 6.557, 0), ((0, 0), (4, 0))),
                                      ((2039, 2442), (37707962, 44264502, 6.557, 0), ((1, 0), (4, 1))),
                                      ((2442, 2542), (44264502, 44930087, 0.666, 0), ((0, 1), (3, 0), (5, 0), (2, 0))),
                                      ((2442, 2542), (44264502, 44930087, 0.666, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2442, 2542), (44264502, 44930087, 0.666, 0), ((1, 0), (4, 1))),
                                      ((2542, 2642), (44930087, 45823327, 0.893, 0), ((0, 1), (3, 0), (4, 0), (5, 0), (2, 0))),
                                      ((2542, 2642), (44930087, 45823327, 0.893, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2542, 2642), (44930087, 45823327, 0.893, 0), ((1, 0), (4, 1))),
                                      ((2642, 2742), (45823327, 47169675, 1.346, 0), ((0, 1), (3, 0), (5, 0), (4, 0))),
                                      ((2642, 2742), (45823327, 47169675, 1.346, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2642, 2742), (45823327, 47169675, 1.346, 0), ((1, 0), (4, 1))),
                                      ((2742, 2942), (47169675, 48530211, 1.361, 0), ((0, 1), (3, 0), (5, 0), (4, 0))),
                                      ((2742, 2942), (47169675, 48530211, 1.361, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2742, 2942), (47169675, 48530211, 1.361, 0), ((2, 0), (0, 0))),
                                      ((2742, 2942), (47169675, 48530211, 1.361, 0), ((1, 0), (4, 1))),
                                      ((2942, 3042), (48530211, 49168613, 0.638, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((2942, 3042), (48530211, 49168613, 0.638, 0), ((0, 1), (3, 0), (4, 0))),
                                      ((2942, 3042), (48530211, 49168613, 0.638, 0), ((2, 0), (0, 0))),
                                      ((2942, 3042), (48530211, 49168613, 0.638, 0), ((1, 0), (4, 1))),
                                      ((3042, 3218), (49168613, 51156933, 1.988, 0), ((5, 1), (3, 1), (1, 1), (2, 1))),
                                      ((3042, 3218), (49168613, 51156933, 1.988, 0), ((0, 1), (3, 0), (4, 0))),
                                      ((3042, 3218), (49168613, 51156933, 1.988, 0), ((2, 0), (0, 0), (5, 0))),
                                      ((3042, 3218), (49168613, 51156933, 1.988, 0), ((1, 0), (4, 1)))],
                                     full_data=True, decimal=3, err_msg='Wrong IBD segments, grouped')
        stats = np.array([(len(s.samples), s.length) for s in m])
        best_segment = np.lexsort((-stats[:, 1], -stats[:, 0]))[0]
        assert_equal(best_segment, 26, 'Wrong best segment (IBD set size + length)') 
        # assert_almost_equal(m[best_segment].length, 9.15, decimal=2, err_msg='Wrong best segment (IBD set size + length)')
        # assert_equal(m[best_segment].samples, set([(4, 1), (1, 1), (2, 1)]), err_msg='Wrong best segment (IBD set size + length)')

    def test_match_maternal(self):
        '''Test hashing the rows of a haplotype matrix with the match() function. Here H is n x s.'''
        pass

    def test_parent_segments(self):
        '''Test computing GERMLINE IBD segments between the parents.'''
        m = self.ibd_computer.ibd_segments(ig._HapMatrix(self.problem, self.family.parents)).group_to_disjoint() 
        assert_equal(m.length, 0, 'Wrong best segment (IBD set size + length)') 
    
    #---------------------------------------------
    # Private Methods
    #---------------------------------------------
