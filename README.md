# Simulating-and-pricing-financial-options
Ce projet utilise les méthodes de Monte Carlo pour simuler des mouvements browniens et évaluer le prix d'options financières (européennes et asiatiques), offrant une approche pratique pour comprendre la tarification des produits dérivés.

# Monte Carlo Option Pricing

This project demonstrates the use of Monte Carlo simulations to price European and Asian call options. It also includes simulations of Brownian and Geometric Brownian motions, which are fundamental to modeling stock prices.

## Features

- **Brownian Motion**: Simulates standard Brownian motion.
- **Geometric Brownian Motion**: Simulates geometric Brownian motion, commonly used to model stock prices.
- **European Call Option Pricing**: Uses Monte Carlo simulation to price a European call option.
- **Asian Call Option Pricing**: Uses Monte Carlo simulation to price an Asian call option, which depends on the average price of the underlying asset over a certain period.

## Files

- `Brownian Motion.txt`: Contains functions to simulate Brownian motion.
- `Geometric Brownian Motion.txt`: Contains functions to simulate Geometric Brownian motion and price options.
- `Price of a European Call Option with Monte Carlo.txt`: Contains functions to price a European call option using Monte Carlo simulation.
- `Price of an Asian Call Option with Monte Carlo.txt`: Contains functions to price an Asian call option using Monte Carlo simulation.

## Usage

1. **Simulate Brownian Motion**:
   - Use the `brownian` function to simulate and plot Brownian motion.

2. **Simulate Geometric Brownian Motion**:
   - Use the `geometricbrownian` function to simulate and plot Geometric Brownian motion.

3. **Price European Call Option**:
   - Use the `europeancalloption` function to price a European call option.

4. **Price Asian Call Option**:
   - Use the `asiancalloption` function to price an Asian call option.
