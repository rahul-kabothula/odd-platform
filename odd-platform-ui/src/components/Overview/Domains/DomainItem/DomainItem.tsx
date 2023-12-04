import React, { type FC } from 'react';
import { Box } from '@mui/material';
import type { DataEntityDomain } from 'generated-sources';
import { IconicInfoBadge } from 'components/shared/elements';
import { FolderIcon } from 'components/shared/icons';
import { useIsEmbeddedPath } from 'lib/hooks/useAppPaths/useIsEmbeddedPath';
import { dataEntityDetailsPath } from 'routes';

interface DomainItemProps {
  domain: DataEntityDomain['domain'];
  childrenCount: DataEntityDomain['childrenCount'];
}

const DomainItem: FC<DomainItemProps> = ({ domain, childrenCount }) => {
  const { updatePath } = useIsEmbeddedPath();

  return (
    <IconicInfoBadge
      name={domain.internalName ?? domain.externalName ?? ''}
      count={childrenCount}
      to={updatePath(dataEntityDetailsPath(domain.id))}
      icon={
        <Box
          sx={{
            backgroundColor: 'white',
            padding: 0.5,
            borderRadius: 2,
            display: 'flex',
          }}
        >
          <FolderIcon width={24} height={24} />
        </Box>
      }
    />
  );
};

export default DomainItem;
