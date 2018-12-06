module ExerciseDist where

import Data.Time

-- | Available slots
--
nr_slots :: Int
nr_slots = 7

-- | Given exercises 
--
exercise_bundle :: [(Int, String)]
exercise_bundle = [
        (21, "Skills"), 
        (39, "Techniques"), 
        (18, "Proofs"), 
        (27, "Structure"), 
        (20, "Polymorphism"), 
        (25, "Algorithm"), 
        (1, "Mixed"), 
        (9, "Lambda")
    ]


-- | Prepare buckets of given number
--
prepare_buckets :: Int -> [[(Int, String)]]
prepare_buckets n = [[] | x <- [1..n]]

-- | Exercise buckets
--
exercise_buckets :: [[(Int, String)]]
exercise_buckets = prepare_buckets nr_slots

-- | Find total number of exercises
--
total_count :: [(Int, String)] -> Int
total_count = foldr ((+) . fst) 0

-- | Places a task of a type once in each available bucket
--
-- Examples:
--
-- >>> distribute_tasks (2, "C") [[],[]] []
-- ([[(1,"C")],[(1,"C")]],(0,"C"))
--
-- >>> distribute_tasks (3, "C") [[],[]] []
-- ([[(1,"C")],[(1,"C")]],(1,"C"))
--
-- >>> distribute_tasks (1, "C") [[],[]] []
-- ([[],[(1,"C")]],(0,"C"))
--
-- >>> distribute_tasks (3, "C") [[(1, "K")],[(1, "G")]] []
-- ([[(1,"K"),(1,"C")],[(1,"G"),(1,"C")]],(1,"C"))
--
distribute_tasks :: (Int, String) -> [[(Int, String)]] -> [[(Int, String)]] -> ([[(Int, String)]], (Int, String))
distribute_tasks (0, s) bs acs = ((bs ++ acs), (0,s)) 
distribute_tasks t [] acs = (acs, t)
distribute_tasks (a, s) (b:bs) acs = distribute_tasks (a-1, s) bs (acs ++ [b ++ [(1, s)]])

-- | Spreads the bundle by layered distribution over the available buckets
--
-- Remarks: 
-- | On odd number of "iterations" results in swapped placement
--
-- Examples:
--
-- >>> spread_bundle [(1,"C"), (1,"B")] [[],[]]
-- [[(1,"C")],[(1,"B")]] 
--
-- >>> spread_bundle [(1,"C"), (1,"B"), (1,"A")] [[],[]]
-- [[(1,"B")],[(1,"C"),(1,"A")]] 
--
-- >>> spread_bundle [(2,"C"), (1,"B"), (1,"A")] [[],[]]
-- [[(1,"C"),(1,"B")],[(1,"C"),(1,"A")]] 
--
-- >>> spread_bundle [(4,"C"), (1,"B"), (1,"A")] [[],[]]
-- [[(1,"C"),(1,"C"),(1,"B")],[(1,"C"),(1,"C"),(1,"A")]] 
--
spread_bundle :: [(Int, String)] -> [[(Int, String)]] -> [[(Int, String)]]
spread_bundle [] bs = bs
spread_bundle ((0, s):ts) bs = spread_bundle ts bs
spread_bundle ((a, s):ts) bs = let (mbs,(a1, _)) = distribute_tasks (a,s) bs []
                                in spread_bundle ((a1, s):ts) mbs 
                                    



main = do   putStrLn "How many time slots?" 
            n <- readLn
            let result = spread_bundle exercise_bundle (prepare_buckets n)
                in putStrLn (show (result))
