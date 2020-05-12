MATRIX COMPUTATIONS
In this problem, you will write functions to perform the following matrix operations:
Transpose
Matrix Multiplication
Determinants (for extra credit)
Matrices are represented as a list of list of integers in row major form. For example,
val m5 = List(List(1,2,3,4),List(2,3,5,6),List(7,1,2,4))
represents the matrix:
1 2 3 4
2 3 5 6 
7 1 2 4
Here are the starter files. You need to complete the functions in Matrix.scala. I have documented the functions and several of these are helper functions which I found useful in my solution. You may choose to implement these, but if you come up with other ways to solve transpose, matrixMultiply, and determinant, then you may delete any helper functions that you do not use and include your own helper functions. Make sure Driver program produces correct answer.
Matrix.scala

Driver.scala

Here is a sample run:

macbook-pro:files raj$ scala Driver
List(3, 6)
List(List(2, 3), List(5, 6))
List(List(1, 4), List(2, 5), List(3, 6))
List(List(19, 22), List(43, 50))
List(List(36, 17, 29, 42), List(66, 35, 59, 84))
-306
14
99
0
SONG LYRICS
In this problem you will read a text file containing the lyrics of a song (assume no blank lines in the lyrics) and store each word that appears in the song in a map whose key is the word and the value is a list of positions where the word appears in the lyric (starting at 1). If the word appears at the end of a line, you should store the negative of the position to indicate end of line. Then, using the map you will produce the following output:
display the map
display the lyrics
Total number of unique words in the song
Most frequent word (if there is a tie, display any one of them)
Here is a sample file, song1.txt:
What have I
What have I
What have I done to deserve this
and here is a sample run of the program:
macbook-pro:hq4 raj$ scala SongLyrics song1.txt

Map:

THIS	[-13]
HAVE	[2, 5, 8]
I	[-3, -6, 9]
DONE	[10]
WHAT	[1, 4, 7]
TO	[11]
DESERVE	[12]

Song:

WHAT HAVE I
WHAT HAVE I
WHAT HAVE I DONE TO DESERVE THIS

The number of unique words in the lyric is: 7

Most frequent word: HAVE

Here is the starter file in which I have already written some functions. You need to complete the incomplete functions. Also two sample song files are given.
SongLyrics.scala

song1.txt

song2.txt

The functions in this assignment are self explanatory; so I have not given any explanations. The input parameters and the output types should give you a clear picture of what the functions are supposed to do.