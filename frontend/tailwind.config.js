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
            },
            colors: {
                cblue: {
                    light: '#74BEE9',
                    DEFAULT: '#0071BC',
                    dark: '#004A80',
                },
                cgreen: {
                    DEFAULT: '#88c23d',
                    dark: '#588527',
                },
                cgray: '#414042',
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