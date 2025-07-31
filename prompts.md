## Section 1: Basic Factual Questions

Q1: How many games did Syracuse play in the 2024–25 season?

LLM Answer: 32

Evaluation: Correct (verified from source)


Q2: Who scored the most total points this season?

LLM Answer: Player A with 520 points

Evaluation: Correct (manually confirmed from dataset)


Q3: What was the team’s win-loss record?

LLM Answer: 19–13

Evaluation: Correct (confirmed on stats page)


## Section 2: Analytical Questions


Q4: Who was the most improved player this season?

LLM Answer (initial): Player B, based on late-season performance

Evaluation: Incomplete — no metric used

Fix: Provided first 5-game and last 5-game averages manually

Prompt: “Here are PPG in first 5 vs. last 5 games for each player...”

Updated LLM Answer: Player C (increased from 4.2 PPG to 14.3 PPG)

Final Evaluation: Correct when guided with metrics


Q5: What was the team’s average margin of victory?

LLM Answer: Couldn’t calculate from limited input

Evaluation: Required feeding game-by-game scores

Manually computed in Python to confirm answer


## Section 3: Strategic/Decision-Based Questions
Q6: Should the coach focus on offense or defense to win 2 more games next season?

LLM Answer (initial): Generic advice (e.g., “balance both”)

Fix: Provided avg points scored in wins (78) vs. losses (65), and opponent PPG in losses (80)

Refined Answer: Focus on defense, especially limiting opponents’ second-chance points

Evaluation: Sound reasoning when prompted with supporting stats


Q7: Which one player should the coach work with to be a game-changer next season?

LLM Answer: Player D (leading scorer)

Evaluation: Shallow answer

Fix: Gave LLM context on clutch performance, FT%, minutes played in close games

Final Answer: Player E — consistently efficient but underused; promising upside

Evaluation: Acceptable recommendation with reasoning


## Prompt Engineering Notes

Prompted LLM using tables and breakdowns to assist reasoning

For improvement-related prompts, LLM needed structured before/after metrics

For strategy questions, supplying win/loss splits enabled stronger logic

For player performance, used terms like “clutch performance,” “efficiency rating,” “bench minutes” to guide the model’s attention
