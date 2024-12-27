#!/usr/bin/env python
# coding: utf-8

# ## Importing Required Libraries

# In[42]:


import pandas as pd
import openai
import ast


# ## Enabling GenAI

# In[43]:


key = "#Paste your API key here"
openai.api_key = key
openai.models.list()


# In[44]:


from openai import OpenAI
client = OpenAI(api_key = key)


# ## Importing Data from the TXT and converting it to List

# In[45]:


with open('Food Data.txt', 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()
    literals = []

    for line in lines:
        literals.append(ast.literal_eval(f'"{line.strip()}"'))

literals


# ## Function Calling Tool

# In[46]:


tools = [
        {
            "type": "function",
            "function": {
                "name": "get_customer_info",
                "description": "Get the customer information from the text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the customer"
                        },
                        "fav_food": {
                            "type": "string",
                            "description": "Favorite food ordered"
                        },
                        "fav_restaurant": {
                            "type": "string",
                            "description": "Favorite restaurant of customer"
                        },
                        "total_amt": {
                            "type": "string",
                            "description": "Total amount spent"
                        },
                        "city": {
                            "type": "string",
                            "description": "City customer belongs to"
                        }
                    }
                }
            }
        }
    ]


# ## Converting the list to individual dictionaries and appending into one

# In[47]:


dfs = []

for s in literals:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": s
        }
      ],
        tools=tools
    )

    res = response.choices[0].message.tool_calls[0].function.arguments
    my_dict = ast.literal_eval(res)
    my_dict
    dfs.append(my_dict)


# In[48]:


dfs


# In[49]:


final_df = pd.DataFrame(dfs)
final_df


# In[50]:


def get_restaurant_suggestion(fav_food, city):
    try:
        # Make a request to the OpenAI API to get restaurant suggestions
        response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
        {
          "role": "user",
          "content": f'''Can you suggest 1 top restaurant which serves the best {fav_food} in {city}.
          Can you please answer with just the restaurant name and nothing else''',
        }
      ],
        max_tokens=30
    )
        # Check if the API response is valid
        if response.choices and response.choices[0].message and response.choices[0].message.content:
            suggestion = response.choices[0].message.content
            suggested_restaurant = suggestion.split(':')[0].strip()
            return suggested_restaurant
        else:
            return 'No suggestion found'
    except Exception as e:
        print(f"Error fetching suggestion: {e}")
        return 'Error fetching suggestion'

# Create an empty list to store restaurant names
suggested_restaurant = []

# Iterate over each row in the DataFrame using a for loop
for index, row in final_df.iterrows():
    fav_food = row['fav_food']
    city = row['city']
    name = get_restaurant_suggestion(fav_food, city)
    suggested_restaurant.append(name)

# Add the restaurant names as a new column in the DataFrame
final_df['suggested_restaurant'] = suggested_restaurant


# In[51]:


final_df


# In[ ]:




