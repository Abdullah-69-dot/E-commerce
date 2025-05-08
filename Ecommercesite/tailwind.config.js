/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html',
    './products/templates/**/*.html',
    './cart/templates/**/*.html',
  ],
  safelist: [
    "bg-red-600",
    "hover:bg-red-700",
    "focus:ring-red-400",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

