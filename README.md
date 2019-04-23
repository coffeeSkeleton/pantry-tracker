# pantry-tracker

4/22: New Non-Linear Formatting lets you view all your options, select one, and go back and select other options! Also:
  - cleaned up some redundant code
  - fixed a bug caused when item buydate and usedate were the same

4/20: The program now does the following:
- allows you to add new items to an external list
- adds item's purchase date, price, and name, as well as an eventual final-use date
- creates a custom class for these items with the above criterion as attributes
- calculates value of item as determined by price/(buydate-usedate)

Future update ideas:
- allow items to be removed
- deal with multiple items with the same name, and how to calulate a mean value (more advanced database than .txt file needed)
