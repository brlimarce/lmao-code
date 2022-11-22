import Button from '@mui/material/Button'

export default function IconButton({
  color,
  icon,
  slot,
  handleClick = () => {},
  component = '',
}) {
  return (
    <Button
      variant="outlined"
      color={color}
      component={component}
      startIcon={icon}
      onClick={handleClick}
      sx={{
        marginRight: '1rem',
        fontWeight: 700,
      }}
      disableElevation
      fullWidth
    >
      {slot}
    </Button>
  )
}
