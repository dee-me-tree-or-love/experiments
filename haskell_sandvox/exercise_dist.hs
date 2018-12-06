import Data.Time

{-
    Distribute exercises from the given set more or less evenly
-}


{-
    Available slots
-}
nr_slots :: Int
nr_slots = 7

{- 
    Given exercises 
-}
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

{-
    Find total number of exercises
-}
total_count :: [(Int, String)] -> Int
total_count = foldr ((+) . fst) 0

{-
    Minimal required slot size
-}
min_slot_size :: Int
min_slot_size = ceiling (t / n) 
                    where   
                        t = (fromIntegral . total_count) exercise_bundle
                        n = fromIntegral nr_slots


{-
    Example: 
    
    >>>  distribute_tasks (2, "C") [[],[]] []
    [[(1, "C")], [(1,"C")]]
-}

distribute_tasks :: (Int, String) -> [[(Int, String)]] -> [[(Int, String)]] -> [[(Int, String)]]
distribute_tasks (0, _) bs acs = bs ++ acs
distribute_tasks _ [] acs = acs
distribute_tasks (a, s) (b:bs) acs = distribute_tasks (a-1, s) bs (acs ++ [b ++ [(1, s)]])

main = do putStrLn "whatever"