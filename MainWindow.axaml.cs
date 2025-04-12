using System;
using System.Net.Mime;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml.Styling;

namespace Shinys_Ultimate_Mod_Manager;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        Theme.SelectionChanged += ThemeSelector_SelectionChanged;
    }

    private void ThemeSelector_SelectionChanged(object? sender, SelectionChangedEventArgs e)
    {
        if (Theme.SelectedItem is ComboBoxItem { Content: string selectedTheme })
        {
            ApplyTheme(selectedTheme);
        }
    }

    private void ApplyTheme(string selectedTheme)
    {
        var styles = Application.Current?.Styles;

        if (styles is { Count: > 1 })
        {
            styles.RemoveAt(1);
        }

        var url = selectedTheme switch
        {
            "Light" => new Uri("avares://Shinys_Ultimate_Mod_Manager/Themes/LightTheme.axaml"),
            "Dark" => new Uri("avares://Shinys_Ultimate_Mod_Manager/Themes/DarkTheme.axaml"),
            "System" => GetSystemThemeUri(),
            _ => null
        };

        if (url is null) return;
        var theme = new StyleInclude(new Uri("resm:Styles?assembly=Shinys_Ultimate_Mod_Manager"))
        {
            Source = url
        };
        styles?.Insert(1, theme);
    }

    private Uri? GetSystemThemeUri()
    {
        //TODO: add detection for system theme.
        return new Uri("avares://Shinys_Ultimate_Mod_Manager/Themes/DarkTheme.axaml");
    }
}