import Data.Time.Clock
import Data.Time.Calendar
import System.Process


-- gets the current date
currentDate :: IO (Integer,Int,Int) -- :: (year,month,day)
currentDate = getCurrentTime >>= return . toGregorian . utctDay


-- creates shell file used to execute commits
createShell :: String -> IO ()
createShell fileName = do    
    writeFile fileName "echo \"hehe\""

-- executes the created shell file
executeShell :: String -> IO ()
executeShell str = do 
    x <- readProcessWithExitCode "sh" [str] ""
    print x

main :: IO ()
main = let fileName = "example.sh" in do
    date <- currentDate
    print date
    createShell fileName 
    executeShell fileName
