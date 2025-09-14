import { usePathname } from 'next/navigation';

import { Dna, Pill, Terminal, Home} from 'lucide-react';

export const NavItems = () => {
  const pathname = usePathname();

  function isNavItemActive(pathname: string, nav: string) {
    return pathname.includes(nav);
  }

  return [
    {
      name: 'Home',
      href: '/',
      icon: <Home size={20} />,
      active: pathname === '/',
      position: 'top',
    },
    {
      name: 'Genes',
      href: '/genes',
      icon: <Dna size={20} />,
      active: isNavItemActive(pathname, '/genes'),
      position: 'top',
    },
    {
      name: 'Drugs',
      href: '/drugs',
      icon: <Pill size={20} />,
      active: isNavItemActive(pathname, '/drugs'),
      position: 'top',
    },
    {
      name: 'Run Pharmcat',
      href: '/run-pharmcat',
      icon: <Terminal size={20} />,
      active: isNavItemActive(pathname, '/run-pharmcat'),
      position: 'top',
    },
    // {
    //   name: 'Settings',
    //   href: '/settings',
    //   icon: <Settings size={20} />,
    //   active: isNavItemActive(pathname, '/settings'),
    //   position: 'bottom',
    // },
  ];
};
