# fix-list
Fixes list formatting

Accepts the filename of an incorrectly formatted list and outputs the formatted list.

The script fix-list.py assumes the following to be the syntax of a correctly formatted list item:
 it begins with a number followed by a dot followed by a space followed by any number of non-digit characters.

It is assumed that if a number is present within a list item(and that number is not denoting the item number) then that means there's a formatting problem: two items on a single line. which is then corrected by this script. Hence, there can't be numbers within the list item. It is easy to change the script appropriately to remove this behaviour

If the characters after the item number are not '.' and not alphanumeric, then they are removed.

The script also automatically capitalizes all the words. This behaviour can be removed by removing the line which calls the 'title' method. Replacing the title method with the method 'capiitalize' will capitalize only the first letter of the list item.
