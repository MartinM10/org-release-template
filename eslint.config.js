import js from '@eslint/js'

export default [
    js.configs.recommended,
    {
        files: ['**/*.js'],
        languageOptions: {
            ecmaVersion: 2024,
            sourceType: 'module',
            globals: {
                console: 'readonly',
                process: 'readonly',
                module: 'readonly',
                require: 'readonly',
                __dirname: 'readonly',
                __filename: 'readonly',
                exports: 'readonly'
            }
        },
        rules: {
            'no-unused-vars': 'warn',
            'no-console': 'off',
            'semi': ['error', 'never'],
            'quotes': ['error', 'single'],
            'indent': ['error', 2],
            'comma-dangle': ['error', 'never'],
            'eol-last': ['error', 'always']
        }
    },
    {
        ignores: ['node_modules/**', 'dist/**', 'coverage/**']
    }
]
