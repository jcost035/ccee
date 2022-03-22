// const colors = require('tailwindcss/colors')

module.exports = {
    theme: {
        extend: {
            screens: {
                '3xl': '1920px',
              },
            minHeight: {

                '0': '0',
         
                '1/4': '25%',

                '1/3': '33%',
         
                '1/2': '50%',
         
                '3/4': '75%',
         
                'full': '100%',
               },
            zIndex: {
                '-1': '-1',
                '100': '100',
            },
            transitionProperty: {
                'height': 'height',
                'padding': 'padding',
                'margin': 'margin',
                'display': 'display'
            },
            spacing: {
                '90': '22rem',
                '100': '30rem',
                '128': '32rem',
                '140': '37rem',
                '150': '38.5rem',
                '175': '45rem',
                '135': '32.7rem',
                '37': '37%',
                '200': '52rem',
                '256': '62rem',
                '170': '1700px',
                '190': '70vh',
                '60vh': '60vh',
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
                gblue: '#0c4b7f',
                ggold: '#d8ad50'
            },
            letterSpacing: {
                widester: '.35em',
            },
            fontFamily: {
                'bebas': ['Bebas\\ Neue', 'cursive'],
                'roboto': ['Roboto\\ Condensed', 'sans-serif'],
                'limelight': ['Limelight', 'cursive']
            },
            height: {
                tile: '30vh'
            },
            screens: {
                'large-border': { 'min': '2080px' },

                'm-large-border': { 'max': '2080px' },

                'small-border': { 'min': '1300px' },

                'm-small-border': { 'max': '1300px' },
                // => @media (max-width: 1300px) { ... }

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
    purge: {
        enabled: false,
        content: ['./templates/**/*.html',
            './polls/templates/**/*.html'
        ],

    },
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