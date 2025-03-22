from flask import Flask, render_template
# from .app.extra_functions import limit_numeric_to_2_decimals
# from .app.data_analysis_classes import DataAnalysis
# from app.Read_supabase_data import *
import pandas as pd
import json
import os


PER_PAGE = 10  # Number of riders per page

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard(page = 1):
    # Data fetch
    start_idx = (page - 1) * PER_PAGE
    end_idx = start_idx + PER_PAGE

    avg_lap = []  
    fast_lap = []  
    slow_lap = []  
    badman = []  
    diesel = []  
    electric = [] 

    avg_lap_cut = avg_lap[start_idx:end_idx]
    total_riders = len(avg_lap)
    total_pages = (total_riders + PER_PAGE - 1) // PER_PAGE  
    next_page = page + 1 if page < total_pages else 1  
    prev_page = page - 1 if page > 1 else total_pages

    return render_template('leaderboard.html', 
                            averages=avg_lap, 
                            top_laps=fast_lap, 
                            slow_lap=slow_lap, 
                            badman_lap=badman,
                            diesel=diesel,
                            electric=electric,
                            page = page)

    return redirect(url_for('index'))

@app.route('/start_session')
def start_session():
    return render_template('start_session.html')

@app.route('/stop_session')
def stop_session():
    return render_template('stop_session.html')

@app.route('/generate_report')
def generate_report():
    return render_template('generate_report.html')

@app.route('/names')
def names():
    return render_template('names.html')

if __name__ == '__main__':
    app.run(debug=True)