import streamlit as st
import random

# def create_dict():
#     # Step 1: Ask for user input on the context
#     context = input("Enter the context (e.g., UTG fold, LJ fold, ... BB (Hero) Action): ")
#
#     # Step 2: Create an empty dictionary to store actions and their ranges
#     dic = {"context": context, "actions": {}}
#
#     while True:
#         # Step 3: Ask for action type (e.g., Call 2.5bb or Raise 13bb)
#         action = input("Enter action name (e.g., 'Call 2.5bb' or 'Raise 13bb') or 'q' to quit: ")
#         if action.lower() == 'q':
#             break
#
#         # Step 4: Ask for the range in the specified format
#         range_input = input(f"Enter the range for {action} (e.g., ATs:0.65, A9s:1.0, ...): ")
#
#         # Step 5: Convert the range input to a dictionary
#         range_dict = {}
#         for item in range_input.split(","):
#             hand, value = item.split(":")
#             range_dict[hand.strip()] = float(value.strip())
#
#         # Step 6: Add the action and its corresponding range to the bb_defend dictionary
#         dic["actions"][action] = range_dict
#
#     return dic
#
#
# # Example usage
# dic = create_dict()
# print(dic)

starting_hands = [
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A9o", "A8s", "A8o",
    "A7s", "A7o", "A6s", "A6o", "A5s", "A5o", "A4s", "A4o", "A3s", "A3o", "A2s", "A2o",
    "KQs", "KQo", "KJs", "KJo", "KTs", "KTo", "K9s", "K9o", "K8s", "K8o", "K7s", "K7o",
    "K6s", "K6o", "K5s", "K5o", "K4s", "K4o", "K3s", "K3o", "K2s", "K2o",
    "QJs", "QJo", "QTs", "QTo", "Q9s", "Q9o", "Q8s", "Q8o", "Q7s", "Q7o", "Q6s", "Q6o",
    "Q5s", "Q5o", "Q4s", "Q4o", "Q3s", "Q3o", "Q2s", "Q2o",
    "JTs", "JTo", "J9s", "J9o", "J8s", "J8o", "J7s", "J7o", "J6s", "J6o", "J5s", "J5o",
    "J4s", "J4o", "J3s", "J3o", "J2s", "J2o",
    "T9s", "T9o", "T8s", "T8o", "T7s", "T7o", "T6s", "T6o", "T5s", "T5o", "T4s", "T4o",
    "T3s", "T3o", "T2s", "T2o",
    "98s", "98o", "97s", "97o", "96s", "96o", "95s", "95o", "94s", "94o", "93s", "93o",
    "92s", "92o",
    "87s", "87o", "86s", "86o", "85s", "85o", "84s", "84o", "83s", "83o", "82s", "82o",
    "76s", "76o", "75s", "75o", "74s", "74o", "73s", "73o", "72s", "72o",
    "65s", "65o", "64s", "64o", "63s", "63o", "62s", "62o",
    "54s", "54o", "53s", "53o", "52s", "52o",
    "43s", "43o", "42s", "42o",
    "32s", "32o"
]



UTG_RFI = {'context': 'UTG (Hero)...', 'actions': {'Bet 2bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 1.0, 'A8s': 1.0, 'A7s': 1.0, 'A6s': 1.0, 'A5s': 1.0, 'A4s': 1.0, 'A3s': 1.0, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 1.0, 'K8s': 0.79, 'K7s': 0.585, 'K6s': 0.465, 'K5s': 0.205, 'AQo': 1.0, 'KQo': 1.0, 'QQ': 1.0, 'QJs': 1.0, 'QTs': 1.0, 'Q9s': 1.0, 'Q8s': 0.035, 'AJo': 1.0, 'KJo': 0.615, 'QJo': 0.35, 'JJ': 1.0, 'JTs': 1.0, 'J9s': 1.0, 'ATo': 0.755, 'KTo': 0.05, 'TT': 1.0, 'T9s': 1.0, 'T8s': 0.44, '99': 1.0, '98s': 0.375, '97s': 0.01, '88': 1.0, '87s': 0.18, '77': 1.0, '76s': 0.165, '66': 1.0, '65s': 0.205, '55': 0.93, '54s': 0.095, '44': 0.355, '33': 0.325, '22': 0.355}}}
HJ_RFI = {'context': 'UTG folds. HJ (Hero)...', 'actions': {'Bet 2bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 1.0, 'A8s': 1.0, 'A7s': 1.0, 'A6s': 1.0, 'A5s': 1.0, 'A4s': 1.0, 'A3s': 1.0, 'A2s': 1.0, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 1.0, 'K8s': 1.0, 'K7s': 1.0, 'K6s': 1.0, 'K5s': 0.39, 'AQo': 1.0, 'KQo': 1.0, 'QQ': 1.0, 'QJs': 1.0, 'QTs': 1.0, 'Q9s': 1.0, 'Q8s': 0.615, 'AJo': 1.0, 'KJo': 1.0, 'QJo': 1.0, 'JJ': 1.0, 'JTs': 1.0, 'J9s': 1.0, 'J8s': 0.25, 'ATo': 1.0, 'KTo': 0.525, 'QTo': 0.29, 'JTo': 0.335, 'TT': 1.0, 'T9s': 1.0, 'T8s': 1.0, 'A9o': 0.15, '99': 1.0, '98s': 1.0, '97s': 0.145, '88': 1.0, '87s': 0.305, '77': 1.0, '76s': 0.145, '66': 1.0, '65s': 0.19, '55': 1.0, '54s': 0.025, '44': 0.755, '33': 0.455, '22': 0.405}}}
CO_RFI = {'context': 'UTG fold, HJ fold. CO (Hero)...', 'actions': {'Bet 2bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 1.0, 'A8s': 1.0, 'A7s': 1.0, 'A6s': 1.0, 'A5s': 1.0, 'A4s': 1.0, 'A3s': 1.0, 'A2s': 1.0, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 1.0, 'K8s': 1.0, 'K7s': 1.0, 'K6s': 1.0, 'K5s': 1.0, 'K4s': 1.0, 'K3s': 1.0, 'AQo': 1.0, 'KQo': 1.0, 'QQ': 1.0, 'QJs': 1.0, 'QTs': 1.0, 'Q9s': 1.0, 'Q8s': 1.0, 'Q7s': 1.0, 'Q6s': 1.0, 'Q5s': 1.0, 'AJo': 1.0, 'KJo': 1.0, 'QJo': 1.0, 'JJ': 1.0, 'JTs': 1.0, 'J9s': 1.0, 'J8s': 1.0, 'J7s': 1.0, 'ATo': 1.0, 'KTo': 1.0, 'QTo': 1.0, 'JTo': 1.0, 'TT': 1.0, 'T9s': 1.0, 'T8s': 1.0, 'T7s': 0.85, 'A9o': 1.0, 'K9o': 0.178, 'J9o': 0.21, 'T9o': 0.19, '99': 1.0, '98s': 1.0, '97s': 1.0, 'A8o': 0.85, '88': 1.0, '87s': 1.0, '86s': 0.47, '77': 1.0, '76s': 0.584, '66': 1.0, '65s': 0.474, 'A5o': 0.12, '55': 1.0, '54s': 0.216, '44': 1.0, '33': 0.816, '22': 0.774}}}
BU_RFI = {'context': 'UTG fold, HJ fold, CO fold. BU (Hero)...', 'actions': {'Bet 2.5bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 1.0, 'A8s': 1.0, 'A7s': 1.0, 'A6s': 1.0, 'A5s': 1.0, 'A4s': 1.0, 'A3s': 1.0, 'A2s': 1.0, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 1.0, 'K8s': 1.0, 'K7s': 1.0, 'K6s': 1.0, 'K5s': 1.0, 'K4s': 1.0, 'K3s': 1.0, 'K2s': 1.0, 'AQo': 1.0, 'KQo': 1.0, 'QQ': 1.0, 'QJs': 1.0, 'QTs': 1.0, 'Q9s': 1.0, 'Q8s': 1.0, 'Q7s': 1.0, 'Q6s': 1.0, 'Q5s': 1.0, 'Q4s': 1.0, 'Q3s': 1.0, 'Q2s': 1.0, 'AJo': 1.0, 'KJo': 1.0, 'QJo': 1.0, 'JJ': 1.0, 'JTs': 1.0, 'J9s': 1.0, 'J8s': 1.0, 'J7s': 1.0, 'J6s': 1.0, 'J5s': 1.0, 'J4s': 1.0, 'J3s': 0.315, 'ATo': 1.0, 'KTo': 1.0, 'QTo': 1.0, 'JTo': 1.0, 'TT': 1.0, 'T9s': 1.0, 'T8s': 1.0, 'T7s': 1.0, 'T6s': 1.0, 'T5s': 0.305, 'A9o': 1.0, 'K9o': 1.0, 'Q9o': 1.0, 'J9o': 1.0, 'T9o': 1.0, '99': 1.0, '98s': 1.0, '97s': 1.0, '96s': 1.0, 'A8o': 1.0, 'K8o': 0.685, 'J8o': 0.34, 'T8o': 0.955, '98o': 0.685, '88': 1.0, '87s': 1.0, '86s': 1.0, '85s': 0.835, 'A7o': 1.0, 'K7o': 0.275, '77': 1.0, '76s': 1.0, '75s': 1.0, 'A6o': 1.0, '66': 1.0, '65s': 1.0, '64s': 1.0, 'A5o': 1.0, '55': 1.0, '54s': 1.0, '53s': 0.095, 'A4o': 1.0, '44': 1.0, 'A3o': 0.155, '33': 1.0, '22': 1.0}}}
SB_RFI = {'context': 'UTG fold, HJ fold, CO fold, BU fold. SB (Hero)...', 'actions': {'Bet 3bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 1.0, 'A8s': 1.0, 'A7s': 1.0, 'A6s': 1.0, 'A5s': 1.0, 'A4s': 1.0, 'A3s': 1.0, 'A2s': 1.0, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 1.0, 'K8s': 1.0, 'K7s': 1.0, 'K6s': 1.0, 'K5s': 1.0, 'K4s': 1.0, 'K3s': 1.0, 'K2s': 1.0, 'AQo': 1.0, 'KQo': 1.0, 'QQ': 1.0, 'QJs': 1.0, 'QTs': 1.0, 'Q9s': 1.0, 'Q8s': 1.0, 'Q7s': 1.0, 'Q6s': 1.0, 'Q5s': 1.0, 'Q4s': 1.0, 'Q3s': 1.0, 'Q2s': 1.0, 'AJo': 1.0, 'KJo': 1.0, 'QJo': 1.0, 'JJ': 1.0, 'JTs': 1.0, 'J9s': 1.0, 'J8s': 1.0, 'J7s': 1.0, 'J6s': 1.0, 'J5s': 1.0, 'J4s': 1.0, 'J3s': 0.155, 'ATo': 1.0, 'KTo': 1.0, 'QTo': 1.0, 'JTo': 1.0, 'TT': 1.0, 'T9s': 1.0, 'T8s': 1.0, 'T7s': 1.0, 'T6s': 1.0, 'T5s': 0.26, 'A9o': 1.0, 'K9o': 1.0, 'Q9o': 1.0, 'J9o': 1.0, 'T9o': 1.0, '99': 1.0, '98s': 1.0, '97s': 1.0, '96s': 1.0, 'A8o': 1.0, 'K8o': 0.675, 'J8o': 0.205, 'T8o': 0.655, '98o': 0.705, '88': 1.0, '87s': 1.0, '86s': 1.0, '85s': 1.0, 'A7o': 1.0, '87o': 0.425, '77': 1.0, '76s': 1.0, '75s': 1.0, '74s': 0.255, 'A6o': 1.0, '66': 1.0, '65s': 1.0, '64s': 1.0, 'A5o': 1.0, '55': 1.0, '54s': 1.0, '53s': 0.785, 'A4o': 0.945, '44': 1.0, '33': 1.0, '22': 1.0}}}

HJ_vs_UTG_RFI = {'context': 'UTG bet 2bb. HJ (Hero)...', 'actions': {'Raise 6.5bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 1.0, 'A9s': 0.005, 'A8s': 0.13, 'A7s': 0.105, 'A5s': 1.0, 'A4s': 0.725, 'A3s': 0.16, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 1.0, 'KTs': 1.0, 'K9s': 0.05, 'AQo': 1.0, 'KQo': 0.585, 'QQ': 1.0, 'QJs': 0.93, 'QTs': 0.04, 'AJo': 0.015, 'JJ': 1.0, 'JTs': 0.215, 'TT': 1.0, '99': 0.765, '88': 0.41, '77': 0.385, '66': 0.27, '65s': 0.345, '55': 0.095, '54s': 0.24, '44': 0.115, '33': 0.115, '22': 0.075}}}
CO_vs_UTG_RFI = {'context': 'UTG bet 2bb. HJ fold. CO (Hero)...', 'actions': {'Call 2bb': {'AQs': 0.205, 'AJs': 0.295, 'ATs': 0.26, 'A9s': 0.139, 'A8s': 0.095, 'A7s': 0.03, 'A5s': 0.235, 'A4s': 0.185, 'A3s': 0.11, 'AKo': 0.16, 'KQs': 0.275, 'KJs': 0.24, 'KTs': 0.22, 'K9s': 0.065, 'K6s': 0.015, 'AQo': 0.195, 'KQo': 0.025, 'QQ': 0.15, 'QJs': 0.265, 'QTs': 0.31, 'JJ': 0.215, 'JTs': 0.37, 'TT': 0.32, 'T9s': 0.16, '99': 0.425, '98s': 0.085, '88': 0.435, '87s': 0.04, '77': 0.378, '76s': 0.055, '66': 0.275, '65s': 0.115, '55': 0.155, '54s': 0.135, '44': 0.11, '33': 0.105, '22': 0.109}, 'Raise 6.5bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 0.795, 'AJs': 0.705, 'ATs': 0.74, 'A9s': 0.388, 'A8s': 0.27, 'A7s': 0.11, 'A5s': 0.765, 'A4s': 0.665, 'A3s': 0.25, 'AKo': 0.84, 'KK': 1.0, 'KQs': 0.725, 'KJs': 0.76, 'KTs': 0.78, 'K9s': 0.363, 'AQo': 0.805, 'KQo': 0.599, 'QQ': 0.85, 'QJs': 0.735, 'QTs': 0.69, 'AJo': 0.22, 'KJo': 0.07, 'JJ': 0.785, 'JTs': 0.63, 'TT': 0.68, 'T9s': 0.15, '99': 0.575, '88': 0.565, '87s': 0.006, '77': 0.483, '76s': 0.045, '66': 0.315, '65s': 0.405, '55': 0.105, '54s': 0.29, '44': 0.1, '33': 0.07, '22': 0.02}}}
BU_vs_UTG_RFI = {'context': 'UTG bet 2bb. HJ fold, CO fold. BU (Hero)...', 'actions': {'Call 2bb': {'AQs': 0.48, 'AJs': 0.48, 'ATs': 0.605, 'A9s': 0.565, 'A8s': 0.48, 'A7s': 0.385, 'A6s': 0.075, 'A5s': 0.53, 'A4s': 0.43, 'A3s': 0.495, 'A2s': 0.07, 'AKo': 0.295, 'KQs': 0.545, 'KJs': 0.565, 'KTs': 0.74, 'K9s': 0.38, 'K7s': 0.03, 'K6s': 0.26, 'AQo': 0.545, 'KQo': 0.255, 'QQ': 0.295, 'QJs': 0.73, 'QTs': 0.625, 'AJo': 0.215, 'JJ': 0.525, 'JTs': 0.785, 'J9s': 0.375, 'TT': 0.645, 'T9s': 0.67, 'T8s': 0.175, '99': 0.825, '98s': 0.49, '97s': 0.06, '88': 0.8, '87s': 0.366, '86s': 0.035, '77': 0.805, '76s': 0.284, '66': 0.75, '65s': 0.475, '55': 0.7, '54s': 0.57, '44': 0.58, '33': 0.51, '22': 0.565}, 'Raise 7.5bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 0.52, 'AJs': 0.52, 'ATs': 0.395, 'A9s': 0.435, 'A8s': 0.52, 'A7s': 0.615, 'A5s': 0.47, 'A4s': 0.57, 'A3s': 0.505, 'AKo': 0.705, 'KK': 1.0, 'KQs': 0.455, 'KJs': 0.435, 'KTs': 0.26, 'K9s': 0.62, 'K8s': 0.15, 'K7s': 0.04, 'K6s': 0.18, 'AQo': 0.455, 'KQo': 0.745, 'QQ': 0.705, 'QJs': 0.27, 'QTs': 0.375, 'AJo': 0.41, 'KJo': 0.155, 'JJ': 0.475, 'JTs': 0.215, 'KTo': 0.085, 'TT': 0.355, 'T9s': 0.33, 'T8s': 0.085, '99': 0.175, '98s': 0.06, '88': 0.2, '87s': 0.06, '77': 0.195, '76s': 0.085, '66': 0.25, '65s': 0.325, '55': 0.235, '54s': 0.155, '44': 0.205, '33': 0.12, '22': 0.09}}}

BB_defend_vs_BU = {'context': 'UTG fold, HJ fold, CO fold, BU bet 2.5bb. SB fold, BB (Hero)...', 'actions': {'Call 2.5bb': {'ATs': 0.65, 'A9s': 1.0, 'A8s': 0.84, 'A7s': 0.96, 'A6s': 1.0, 'A4s': 0.525, 'A3s': 0.855, 'A2s': 0.9, 'KJs': 0.52, 'KTs': 0.55, 'K9s': 0.705, 'K8s': 0.93, 'K7s': 0.805, 'K6s': 0.735, 'K5s': 0.835, 'K4s': 0.845, 'K3s': 0.92, 'K2s': 1.0, 'AQo': 0.065, 'KQo': 0.635, 'QJs': 0.92, 'QTs': 0.72, 'Q9s': 0.92, 'Q8s': 0.94, 'Q7s': 0.975, 'Q6s': 0.88, 'Q5s': 0.905, 'Q4s': 0.94, 'Q3s': 0.84, 'Q2s': 0.99, 'AJo': 0.605, 'KJo': 0.66, 'QJo': 0.715, 'JTs': 0.275, 'J9s': 0.245, 'J8s': 0.88, 'J7s': 0.605, 'J6s': 0.825, 'J5s': 0.765, 'J4s': 0.82, 'J3s': 0.86, 'J2s': 0.96, 'ATo': 0.745, 'KTo': 0.56, 'QTo': 0.67, 'JTo': 0.755, 'T8s': 0.425, 'T7s': 0.7, 'T6s': 0.56, 'T5s': 0.65, 'T4s': 0.305, 'T3s': 0.33, 'A9o': 0.71, 'K9o': 0.635, 'Q9o': 0.715, 'J9o': 0.835, 'T9o': 0.865, '99': 0.29, '98s': 0.49, '97s': 0.885, '96s': 0.88, '95s': 0.345, 'A8o': 0.825, 'K8o': 0.31, 'T8o': 0.375, '98o': 0.33, '88': 0.675, '87s': 0.52, '86s': 0.95, '85s': 0.87, '84s': 0.045, 'A7o': 0.7, '87o': 0.27, '77': 0.86, '76s': 0.395, '75s': 1.0, '74s': 1.0, 'A6o': 0.285, '76o': 0.275, '66': 1.0, '65s': 0.785, '64s': 1.0, '63s': 1.0, 'A5o': 0.865, '55': 1.0, '54s': 0.65, '53s': 1.0, '52s': 1.0, 'A4o': 0.395, '44': 1.0, '43s': 1.0, '42s': 0.95, '33': 1.0, '32s': 0.235, '22': 1.0}, 'Raise 13bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 1.0, 'AJs': 1.0, 'ATs': 0.35, 'A8s': 0.16, 'A7s': 0.04, 'A5s': 1.0, 'A4s': 0.475, 'A3s': 0.145, 'A2s': 0.1, 'AKo': 1.0, 'KK': 1.0, 'KQs': 1.0, 'KJs': 0.48, 'KTs': 0.45, 'K9s': 0.295, 'K8s': 0.07, 'K7s': 0.195, 'K6s': 0.265, 'K5s': 0.165, 'K4s': 0.155, 'K3s': 0.08, 'AQo': 0.935, 'KQo': 0.365, 'QQ': 1.0, 'QJs': 0.08, 'QTs': 0.28, 'Q9s': 0.08, 'Q8s': 0.06, 'Q7s': 0.025, 'Q6s': 0.12, 'Q5s': 0.095, 'Q4s': 0.06, 'Q3s': 0.16, 'Q2s': 0.01, 'AJo': 0.395, 'KJo': 0.34, 'QJo': 0.285, 'JJ': 1.0, 'JTs': 0.725, 'J9s': 0.755, 'J8s': 0.12, 'J7s': 0.395, 'J6s': 0.175, 'J5s': 0.235, 'J4s': 0.18, 'J3s': 0.14, 'ATo': 0.255, 'KTo': 0.44, 'QTo': 0.33, 'JTo': 0.245, 'TT': 1.0, 'T9s': 1.0, 'T8s': 0.575, 'T7s': 0.3, 'T6s': 0.44, 'A9o': 0.29, 'K9o': 0.365, 'Q9o': 0.19, 'J9o': 0.085, 'T9o': 0.135, '99': 0.71, '98s': 0.51, '97s': 0.115, '96s': 0.12, 'A8o': 0.175, 'K8o': 0.02, '88': 0.325, '87s': 0.48, '86s': 0.05, '85s': 0.13, 'A7o': 0.3, '77': 0.14, '76s': 0.605, 'A6o': 0.05, '65s': 0.215, 'A5o': 0.135, '54s': 0.35, 'A4o': 0.095}}}
BB_defend_vs_UTG = {'context': 'UTG bet 2bb. HJ fold, CO fold, BU fold, SB fold. BB (Hero)...', 'actions': {'Call 2bb': {'AQs': 0.475, 'AJs': 0.745, 'ATs': 0.825, 'A9s': 0.925, 'A8s': 0.94, 'A7s': 0.97, 'A6s': 1.0, 'A5s': 0.81, 'A4s': 0.835, 'A3s': 0.755, 'A2s': 0.68, 'AKo': 0.425, 'KQs': 0.83, 'KJs': 0.9, 'KTs': 0.6, 'K9s': 0.99, 'K8s': 1.0, 'K7s': 0.86, 'K6s': 0.935, 'K5s': 0.88, 'K4s': 0.69, 'K3s': 0.9, 'K2s': 1.0, 'AQo': 1.0, 'KQo': 0.76, 'QQ': 0.345, 'QJs': 0.35, 'QTs': 0.655, 'Q9s': 0.875, 'Q8s': 0.88, 'Q7s': 1.0, 'Q6s': 0.925, 'Q5s': 1.0, 'Q4s': 1.0, 'Q3s': 1.0, 'Q2s': 1.0, 'AJo': 0.995, 'KJo': 0.83, 'QJo': 1.0, 'JJ': 0.87, 'JTs': 0.655, 'J9s': 0.95, 'J8s': 0.98, 'J7s': 1.0, 'J6s': 1.0, 'J5s': 1.0, 'J4s': 1.0, 'J3s': 0.7, 'J2s': 0.47, 'ATo': 0.86, 'KTo': 1.0, 'QTo': 1.0, 'JTo': 1.0, 'TT': 0.965, 'T9s': 0.62, 'T8s': 1.0, 'T7s': 1.0, 'T6s': 1.0, 'T5s': 0.53, 'T4s': 0.415, 'T3s': 0.265, 'A9o': 0.98, 'K9o': 0.32, 'J9o': 0.19, 'T9o': 0.845, '99': 1.0, '98s': 0.775, '97s': 1.0, '96s': 1.0, '95s': 1.0, '93s': 0.265, '92s': 0.28, 'A8o': 0.465, 'T8o': 0.23, '98o': 0.515, '88': 1.0, '87s': 0.55, '86s': 1.0, '85s': 1.0, '84s': 0.605, '97o': 0.155, '87o': 0.605, '77': 1.0, '76s': 0.58, '75s': 1.0, '74s': 1.0, '73s': 0.095, '86o': 0.115, '76o': 0.5, '66': 1.0, '65s': 0.475, '64s': 1.0, '63s': 1.0, 'A5o': 0.43, '65o': 0.495, '55': 1.0, '54s': 0.7, '53s': 1.0, '52s': 1.0, '54o': 0.29, '44': 1.0, '43s': 1.0, '42s': 1.0, '33': 1.0, '32s': 1.0, '22': 1.0}, 'Raise 12bb': {'AA': 1.0, 'AKs': 1.0, 'AQs': 0.525, 'AJs': 0.255, 'ATs': 0.175, 'A9s': 0.075, 'A8s': 0.06, 'A7s': 0.03, 'A5s': 0.19, 'A4s': 0.165, 'A3s': 0.245, 'A2s': 0.32, 'AKo': 0.575, 'KK': 1.0, 'KQs': 0.17, 'KJs': 0.1, 'KTs': 0.4, 'K9s': 0.01, 'K7s': 0.14, 'K6s': 0.065, 'K5s': 0.12, 'K4s': 0.31, 'K3s': 0.1, 'KQo': 0.24, 'QQ': 0.655, 'QJs': 0.65, 'QTs': 0.345, 'Q9s': 0.125, 'Q8s': 0.12, 'Q6s': 0.075, 'AJo': 0.005, 'KJo': 0.17, 'JJ': 0.13, 'JTs': 0.345, 'J9s': 0.05, 'J8s': 0.02, 'ATo': 0.14, 'TT': 0.035, 'T9s': 0.38, 'A9o': 0.02, '98s': 0.225, 'A8o': 0.09, '87s': 0.45, '76s': 0.42, '65s': 0.525, 'A5o': 0.135, '54s': 0.3, 'A4o': 0.045}}}

packs = [UTG_RFI, HJ_RFI, CO_RFI, BU_RFI, SB_RFI, HJ_vs_UTG_RFI, CO_vs_UTG_RFI, BU_vs_UTG_RFI, BB_defend_vs_BU, BB_defend_vs_UTG]
def get_random_hand():
    """Return a random starting hand."""
    return random.choice(starting_hands)

def get_random_pack():
    return random.choice(packs)
def display_strategy(actions, hand):
    """Display action buttons for available actions and fold."""
    st.write(f"Your hand: {hand}")

    # Display buttons for each action
    user_action = None
    for action in actions.keys():
        if st.button(action):
            user_action = action

    # Always show a fold option
    if st.button("Fold"):
        user_action = "Fold"

    return user_action


def check_decision(user_action, hand, actions):
    """Check if the user's action is correct."""

    # Calculate the total frequency of the actions
    total_frequency = sum(
        action_value.get(hand, 0) for action_value in actions.values() if isinstance(action_value, dict))

    # Calculate the folding frequency
    folding_frequency = 1 - total_frequency

    if user_action == "Fold":
        st.write(f"You chose to Fold. The folding frequency for {hand} is {folding_frequency:.2f}.")

        if folding_frequency > 0:
            st.write(f"Correct! Folding is an appropriate decision with {hand}.")
        else:
            st.write(f"Incorrect! You should not fold with {hand}.")

    elif user_action in actions:
        action_frequency = actions[user_action].get(hand, 0)  # Get the frequency for the specific hand

        if action_frequency > 0:
            st.write(f"You chose {user_action} with {hand}. Frequency: {action_frequency:.2f}. Correct!")
        else:
            st.write(
                f"You chose {user_action} with {hand}. Frequency: {action_frequency:.2f}. Incorrect! This action should not be taken with this hand.")
    else:
        st.write(f"You chose {user_action}. This action is not recognized with {hand}. It should be a 100% fold.")
        st.write(f"The folding frequency for {hand} is {folding_frequency:.2f}.")


# Main Streamlit app
def main():
    st.title("Texas Hold'em Starting Hand Decision Trainer")

    # Check if the hand is already in session state, if not generate a new one
    if 'hand' not in st.session_state:
        st.session_state.hand = get_random_hand()
    if 'pack' not in st.session_state:
        st.session_state.pack = get_random_pack()

    # Button to deal a new hand
    if st.button("Deal New Hand"):
        st.session_state.hand = get_random_hand()  # Generate a new random hand
        st.session_state.pack = get_random_pack()
    # Display context
    st.write(st.session_state.pack['context'])

    # Display actions and get user decision
    actions = st.session_state.pack['actions']
    user_action = display_strategy(actions, st.session_state.hand)

    if user_action:
        check_decision(user_action, st.session_state.hand, actions)

if __name__ == "__main__":
    main()
