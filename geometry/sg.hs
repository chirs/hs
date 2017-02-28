module Main where 

main = do writeFile "testFile.txt" "Hello FS"
          putStr "Hello World\n"


-- main = putStr "Hello World\n"

writeFile :: FilePath -> String -> IO ()
type FilePath = String