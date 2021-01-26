// const colors = require('tailwindcss/colors')

module.exports = {
    theme: {
        extend: {
            transitionProperty: {
                'height': 'height'
            }
        },
    },
    purge: [
        './templates/**/*.html',
        './polls/templates/**/*.html'
    ],
    darkMode: false, // or 'media' or 'class'
    variants: {
        extend: {},
    },
    plugins: [],
}