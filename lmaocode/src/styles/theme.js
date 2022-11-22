/**
 * * Theme
 * This contains the standard style guide
 * of the application.
 */
import { createTheme } from '@mui/material/styles'
import { orange } from '@mui/material/colors'
import { styled } from '@mui/material/styles'
import {
  TableCell,
  tableCellClasses,
} from '@mui/material'

// * General
const appTheme = createTheme({
  palette: {
    primary: orange,
  },

  typography: {
    fontFamily: "'Quicksand', sans-serif",
  },

  multilineColor: {
    color: 'white'
  }
})

// * Table Cell
const StyledTableCell = styled(TableCell)(() => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: 'var(--orange-50)',
    color: 'var(--orange-900)',
    fontWeight: 700,
    fontSize: 16,
    textAlign: 'center',
    letterSpacing: '0.02rem',
  },
  [`&.${tableCellClasses.body}`]: {
    textAlign: 'center',
    fontWeight: 500
  },
}))

export { appTheme, StyledTableCell }
