
from flask import Flask, render_template, send_from_directory  
import random
import os

app = Flask(__name__)

# list of 200 quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is 10% what happens to us and 90 how we react to it. - Charles R. Swindoll",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who prepare for it today. - Malcolm X",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "It is never too late to be what you might have been. - George Eliot",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "I attribute my success to this: I never gave or took any excuse. - Florence Nightingale",
    "Our greatest glory is not in never falling, but in rising every time we fall. - Confucius",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You miss 100 of the shots you don't take. - Wayne Gretzky",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "The best revenge is massive success. - Frank Sinatra",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "Eighty percent of success is showing up. - Woody Allen",
    "A journey of a thousand miles begins with a single step. - Lao Tzu",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Problems are not stop signs, they are guidelines. - Robert H. Schuller",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
    "Don't limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve. - Mary Kay Ash",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "You take your life in your own hands, and what happens? A terrible thing, no one to blame. - Erica Jong",
    "It's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "Either you run the day, or the day runs you. - Jim Rohn",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
    "Life is 10% what happens to us and 90 how we react to it. - Charles R. Swindoll",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do. - Mark Twain",
    "When I let go of what I am, I become what I might be. - Lao Tzu",
    "Build your own dreams, or someone else will hire you to build theirs. - Farrah Gray",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "I attribute my success to this: I never gave or took any excuse. - Florence Nightingale",
    "You miss 100 of the shots you don't take. - Wayne Gretzky",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Eighty percent of success is showing up. - Woody Allen",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Problems are not stop signs, they are guidelines. - Robert H. Schuller",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
    "Don't limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve. - Mary Kay Ash",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "You take your life in your own hands, and what happens? A terrible thing, no one to blame. - Erica Jong",
    "It's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "Either you run the day, or the day runs you. - Jim Rohn",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
    "Life is 10% what happens to us and 90 how we react to it. - Charles R. Swindoll",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
]


@app.route('/')
def index():
    # Get a random quote
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# if __name__ == '__main__':
#     app.run(debug=True)
