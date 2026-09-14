export type ThemeMode = 'oled-slate' | 'midnight' | 'light';

export interface ThemeConfig {
  id: ThemeMode;
  name: string;
  description: string;
  badge: string;
}

export const AVAILABLE_THEMES: ThemeConfig[] = [
  {
    id: 'oled-slate',
    name: 'OLED Slate',
    description: 'Ultra-deep dark theme with sleek slate cards and subtle accents (Default)',
    badge: 'OLED Slate'
  },
  {
    id: 'midnight',
    name: 'Minimalist Midnight',
    description: 'Pure black and white monochrome (only black & white boxes and buttons)',
    badge: 'Midnight B&W'
  },
  {
    id: 'light',
    name: 'Clean Light',
    description: 'High-contrast clean daylight reading theme',
    badge: 'Light'
  }
];
