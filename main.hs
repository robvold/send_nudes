import Data.Time.Clock
import Data.Time.Calendar


-- gets the current date
date :: IO (Integer,Int,Int) -- :: (year,month,day)
date = getCurrentTime >>= return . toGregorian . utctDay

-- creates shell file used to execute commits
createShell :: IO ()
createShell = do    
    writeFile "example.sh" "echo \"hehe\""


main :: IO ()
main = do
    x <- date
    print x
    createShell
