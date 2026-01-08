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

/**
 * Multiplies two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The product of a and b
 */
function multiply(a, b) {
  return a * b
}

/**
 * Divides two numbers
 * @param {number} a - Dividend
 * @param {number} b - Divisor
 * @returns {number} The quotient of a and b
 * @throws {Error} When divisor is zero
 */
function divide(a, b) {
  if (b === 0) {
    throw new Error('Cannot divide by zero')
  }
  return a / b
}

/**
 * Formats a semantic version string
 * @param {number} major - Major version
 * @param {number} minor - Minor version
 * @param {number} patch - Patch version
 * @returns {string} Formatted version string
 */
function formatVersion(major, minor, patch) {
  return `v${major}.${minor}.${patch}`
}

module.exports = { greet, add, multiply, divide, formatVersion }

