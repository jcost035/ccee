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
                '128': '32rem',
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
            },
            letterSpacing: {
                widester: '.35em',
            },
            fontFamily: {
                'bebas': ['Bebas\\ Neue', 'cursive'],
                'roboto': ['Roboto\\ Condensed', 'sans-serif']
            },
            height: {
                tile: '30vh'
            },
            screens: {
                'm-2xl': { 'max': '1535px' },
                // => @media (max-width: 1535px) { ... }

                'm-xl': { 'max': '1279px' },
                // => @media (max-width: 1279px) { ... }

                'm-lg': { 'max': '1023px' },
                // => @media (max-width: 1023px) { ... }

                'm-md': { 'max': '767px' },
                // => @media (max-width: 767px) { ... }

                'm-sm': { 'max': '639px' },
                // => @media (max-width: 639px) { ... }
            },

        },

    },
    purge: [
        './templates/**/*.html',
        './polls/templates/**/*.html'
    ],
    darkMode: false, // or 'media' or 'class'
    variants: {
        extend: {
            display: ['hover'],
        },
    },
    plugins: [
        require('@tailwindcss/custom-forms'),
    ],

}