// const colors = require('tailwindcss/colors')

module.exports = {
    theme: {
        extend: {
            zIndex: {
                '-1': '-1'
            },
            transitionProperty: {
                'height': 'height',
                'padding': 'padding',
                'margin': 'margin',
            },
            spacing: {
                '170': '1700px',
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