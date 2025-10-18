/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'dark-bg': '#0b1220',
        'dark-fg': '#e6edf3',
        'dark-muted': '#9fb1c9',
        'dark-accent': '#4aa3ff',
        'dark-card': '#121a2b',
        'dark-border': '#22304a',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
