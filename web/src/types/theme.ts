export type ThemeMode = 'charcoal' | 'midnight' | 'light';

export interface ThemeConfig {
  id: ThemeMode;
  name: string;
  description: string;
  badge: string;
}

export const AVAILABLE_THEMES: ThemeConfig[] = [
  {
    id: 'charcoal',
    name: 'Charcoal Dark',
    description: 'Matte dark grey with pure white typography & sleek contrast (Image style)',
    badge: 'Charcoal'
  },
  {
    id: 'midnight',
    name: 'OLED Midnight',
    description: 'Ultra-deep pitch black with subtle borders',
    badge: 'Midnight'
  },
  {
    id: 'light',
    name: 'Clean Light',
    description: 'High-contrast clean daylight reading theme',
    badge: 'Light'
  }
];
