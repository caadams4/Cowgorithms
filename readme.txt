This program is written in Pythton and hosted on replit. A zip file with the files required will also be provided. 

Execution:

	To execute this file on a linux based system, navigate to the directory that    
  contains the cowgorithms file. Included in this directory must be the file 
  ‘input.txt’ which the program will extract the cow record data. 
	
  Once you ensure the required input.txt file and main.py file are present, type : 
  python3 main.py 
	
  The output will print to the console and write to output.txt.

Overview of Cowgorithms:

  The program executes in a variety of steps.
    1. Open input.txt and read in each row. Convert the data in each row to a dictionary key:val
        Runtime at step 1 : O(r)

    2. Transfer each key:val into a list to sort by lowest weight
        Runtime at step 2 : O(c + r)

    3. Sort list based on 'lowest weight' using built in sorted() method which runs at nlogn according to python documentation.
        Runtime at step 3 : O(2c * logc + r)

    4. Iterate through each cow record to find 'lowest weight' duplicates.
        Runtime at step 4 : O(3c * logc + r)

    5. Sort the 'lowest weight' duplicates in a smaller subset by the 'latest weight'
        Runtime at step 5 : O(4c * logc + r)

    6. Iterate thourhg each 'latest weight' to find duplicates
        Runtime at step 6 : O(5c * logc + r)

    7. Sort the 'latest weight' duplicates in a smaller subset, cut from the 'lowest weight' duplicate set, based on 'average milk production'
        Runtime at step 7 : O(6c * logc + r)

    8. Put the sorted lists back into main sorted list
        Runtime at step 8 : O(6c * log + r)

    9. Copy each cow record to output.txt
        FINAL runtime at step 9 : O(7c * logc + r)
    