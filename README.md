# Get Restaurant Suggestions

This project leverages **OpenAI's GPT-3.5-turbo** to recommend top restaurants based on customer preferences and location. It processes customer data to extract insights and provide personalized dining suggestions.

## Features
- Extracts customer information (e.g., name, favorite food, city, and total spending) from textual data.
- Uses OpenAI's API to suggest the best restaurant for a given cuisine in a specific city.
- Outputs a comprehensive dataset including customer details and corresponding restaurant recommendations.

## Requirements
- **Python 3.7+**
- Libraries: 
  - `pandas`
  - `openai`
  - `ast`

## Setup and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/GetRestaurantSuggestions.git
   ```
2. Install required libraries:
   ```bash
   pip install pandas openai
   ```
3. Replace the placeholder in the script with your OpenAI API key:
   ```python
   key = "#Paste your API key here"
   ```
4. Run the Jupyter Notebook to generate restaurant suggestions.

## Project Workflow
1. **Data Import**:
   - Reads customer data from a `.txt` file.
   - Converts text lines into Python objects for further processing.

2. **Customer Information Extraction**:
   - Extracts details such as customer name, favorite food, preferred restaurant, spending amount, and city using an OpenAI API function tool.

3. **Restaurant Recommendation**:
   - Queries the OpenAI API to recommend top restaurants based on customer preferences.

4. **Output**:
   - Consolidates results into a DataFrame that includes customer details and restaurant suggestions.

## Sample Output
The final output is a DataFrame with the following columns:
- `name`: Customer name
- `fav_food`: Favorite food
- `fav_restaurant`: Favorite restaurant
- `total_amt`: Total amount spent
- `city`: Customer's city
- `suggested_restaurant`: Suggested restaurant for the preferred food in the given city

## Future Enhancements
- Expand the recommendation model to suggest multiple restaurants with detailed ratings and reviews.
- Integrate additional datasets to refine suggestions based on restaurant popularity and availability.
