#Project 6 - Crime Time
#Name: Ajay Patel
#Section 1

import unittest
from crimetime import *
#import crimetime

class TestCases(unittest.TestCase):

   def test_Crime(self):
       crime1 = Crime(101, 'ROBBERY')
       crime2 = Crime(150046641, 'Python')
       crime3 = Crime(101, 'ROBBERY')
       crime2.Day = 'Monday'       
       crime2.Month = 'June'
       crime2.Hour = '11 AM'
       self.assertEqual(crime1.ID, 101)
       self.assertEqual(crime1.Category, 'ROBBERY')
       self.assertEqual(crime2.ID, 150046641)
       self.assertEqual(crime2.Category, 'Python')
       self.assertEqual(crime1.ID == crime3.ID and crime1.Category == crime3.Category, True)
       self.assertEqual(crime2.Day, 'Monday')
       self.assertEqual(crime2.Month, 'June')
       self.assertEqual(crime2.Hour, '11 AM')


   def test_create_crimes(self):
       crime1 = ['150017276\tNON-CRIMINAL\tAIDED CASE', '150023994\tROBBERY\tBODILY FORCE']
       crime2 = ['150046641\tROBBERY', '15000321\tASSAULT\tTHREATS AGAINST LIFE\t12:00', '101\tROBBERY']
       crime3 = ['987\tROBBERY', '234235\tFRAUD\tARMED ASSAILANT', '245\tROBBERY\tKIDNAPPING']
       self.assertListEqual(create_crimes(crime1), [Crime(150023994, 'ROBBERY')])
       self.assertListEqual(create_crimes(crime2), [Crime(150046641, 'ROBBERY'), Crime(101, 'ROBBERY')])
       self.assertListEqual(create_crimes(crime3), [Crime(987, 'ROBBERY'), Crime(245, 'ROBBERY')])


   def test_sort_crimes(self):
       crime1 = [Crime(150046641, 'ROBBERY'), Crime(150097000, 'ROBBERY'), Crime(130045421, 'ROBBERY')] 
       crime2 = [Crime(105, 'ROBBERY'), Crime(2393, 'ROBBERY'), Crime(187, 'ROBBERY')]      
       crime3 = [Crime(12, 'ROBBERY'), Crime(11, 'ROBBERY'), Crime(10, 'ROBBERY')] 
       self.assertListEqual(sort_crimes(crime1), [Crime(130045421, 'ROBBERY'), Crime(150046641, 'ROBBERY'), Crime(150097000, 'ROBBERY')])
       self.assertListEqual(sort_crimes(crime2), [Crime(105, 'ROBBERY'), Crime(187, 'ROBBERY'), Crime(2393, 'ROBBERY')])
       self.assertListEqual(sort_crimes(crime3), [Crime(10, 'ROBBERY'), Crime(11, 'ROBBERY'), Crime(12, 'ROBBERY')])


   def test_find_crime(self):
       crime1 = [Crime(123, 'ROBBERY'), Crime(456, 'ROBBERY'), Crime(789, 'ROBBERY')]
       crime2 = [Crime(1, 'ROBBERY'), Crime(2, 'ROBBERY'), Crime(3, 'ROBBERY')]
       crime3 = [Crime(4, 'ROBBERY'), Crime(5, 'ROBBERY'), Crime(6, 'ROBBERY'), Crime(8, 'ROBBERY')]
       self.assertEqual(find_crime(crime1, 789), Crime(789, 'ROBBERY'))
       self.assertEqual(find_crime(crime2, 1), Crime(1, 'ROBBERY'))
       self.assertEqual(find_crime(crime3, 5), Crime(5, 'ROBBERY'))


   #def test_update_crimes(self):
       #crime1 = [Crime(123, 'ROBBERY')]
       #time1 = ['123\tMONDAY\tJANUARY\t1']
       #self.assertEqual(update_crimes(crime1, time1), Crime(123, 'ROBBERY')) 


     

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
