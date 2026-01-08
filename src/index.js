/**
 * Demo module for the organization template
 * This is a sample file to demonstrate CI/CD workflows
 */

/**
 * Greets a user with a welcome message
 * @param {string} name - The name to greet
 * @returns {string} The greeting message
 */
function greet(name) {
  if (!name || typeof name !== 'string') {
    throw new Error('Name must be a non-empty string')
  }
  return `Hello, ${name}! Welcome to the organization template.`
}

/**
 * Calculates the sum of two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The sum of a and b
 */
function add(a, b) {
  return a + b
}

module.exports = { greet, add }
