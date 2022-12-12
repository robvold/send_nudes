import Data.Time.Clock
import Data.Time.Calendar


-- gets the current date
date :: IO (Integer,Int,Int) -- :: (year,month,day)
date = getCurrentTime >>= return . toGregorian . utctDay

main :: IO ()
main = do
    x <- date 
    print x