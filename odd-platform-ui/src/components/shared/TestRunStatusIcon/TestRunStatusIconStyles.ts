import { styled } from '@mui/material/styles';
import { DataQualityTestRunStatus } from 'generated-sources';
import { propsChecker } from 'lib/helpers';

export const Content = styled('div', {
  shouldForwardProp: propsChecker,
})<{
  $typeName: DataQualityTestRunStatus;
}>(({ theme, $typeName }) => ({
  padding: theme.spacing(0.5),
  marginRight: theme.spacing(1),
  width: '8px',
  height: '8px',
  borderRadius: '50%',
  backgroundColor: theme.palette.reportStatus[$typeName].border,
}));
