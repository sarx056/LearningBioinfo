#!/usr/bin/env python
# coding: utf-8

# # # Welcome to LearningPY!

# In[ ]:


#Week 1 - printing strings, taking inputs, variables, equality function 


# In[1]:


#chingu means friend in korean, i just like it the way it sounds 
print('hello chingus')


# In[2]:


input('whats your age?: ')
print('wow so young')


# In[3]:


#using the equality function 
age = 23 
new_age = 26
print(age == new_age)


# In[4]:


#using the inequality function 
name = 'sara zainab'
mothers_name = 'saleema zainab'
print(name != mothers_name)


# In[6]:


#taking inputs 
fav_food = 'briyani'
user_answer = input('whats your fav food: ')
if user_answer == 'briyani':
    print(True)


# In[3]:


#Project-1: Let's make a smart light switch 
#create a smart light switch that turns off at daytime and turns on at nightime on its own 
#will use is_day as our variable 

is_day = False 
lights_on = not is_day 

print('daytime?')
print(is_day)

print('lights on?')
print(lights_on)


# In[4]:


#vice versa 
is_day = True 
lights_on = not is_day 

print('daytime?')
print(is_day)

print('lights on?')
print(lights_on)


# In[1]:


#I think this previous code, which is the method my app says, is kinda lengthy or not efficient
#making your code work efficiently is important 
#I'm gonna try on my own now 

question = input('Is it daytime or nightime right now?: ')
if question == 'daytime': 
     print('lights off!')
elif question == 'night time': 
    print('lights on!')   
else: 
     print('your choice!')
#see, its short and it works. But ofc this is prolly not how they work in the real world. 


# In[ ]:


#I totally forgot to go over type of values or types in python cuz i've already learned them. Lets go through them once 
Boolean = True 
Boolean_2 = False
String = 'hello world'
string_2 = "hello world x 2 "
int = 45
float = 3.14 


# In[3]:


#converting types and finding what type it is
num = 3 
print(str(num))
print(type(num))


# In[6]:


#lets do more examples 
its_float = 0.999
print(int(its_float))
print(type(its_float))


# In[7]:


im_sara = "True"
print(bool(im_sara))
print(type(im_sara))


# In[14]:


lowercase_name = "kirigan"
lowercase_name.upper()
#uppercase function


# In[16]:


uppercase_name = 'LAYLA' 
uppercase_name.lower()
#lowercase function


# In[17]:


words = "how many letters is this?"
print(len(words))
#length function 


# In[1]:


#check what version of python are we using 
import sys
print(sys.version)


# In[2]:


#string operations 
#indexing 
name = "Sara Zainab"  
print(name[2])


# In[3]:


name = "Oui"
print(name[0])


# In[4]:


#negative indexing 
name = "Sara Zainab"
print(name[-1])


# In[6]:


name = "Michael Jackson"
print(name[-4])


# In[8]:


#slicing
name = 'Sara Zainab'
print(name[0:4])


# In[10]:


name = 'Kim Namjoon'
print(name[4:10])


# In[11]:


#striding: which allows us to select and print certain value from the variable 
name = "Kim Seokjin"
print(name[::2])


# In[13]:


#the backlash allows a range of functions: \n is used for new line 
print('sara is \n the best')


# In[14]:


# \t is used for tab 
print('sara is \t the best')


# In[15]:


# \\ is used for i have no idea lets see 
print('sara is \\ the best')


# In[16]:


# \r is used for also no idea 
print('sara is \r the best')


# In[17]:


print('sara is the \ best')


# In[22]:


#finding dem letters 
name = 'Oui'
print(name.find('ui'))


# In[24]:


name = "Sara Zainab"
print(name.find('nab'))


# In[ ]:




