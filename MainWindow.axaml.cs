using System;
using System.Text;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Mime;
using System.Runtime.InteropServices;
using System.Text.Json;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml.Styling;

namespace Shinys_Ultimate_Mod_Manager;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        
        InitializeComponent();
        
        var savedTheme = LoadSavedTheme();

        if (string.IsNullOrWhiteSpace(savedTheme))
        {
            savedTheme = "System";
        }
        ApplyTheme(savedTheme);
        
        
        Theme.SelectionChanged += ThemeSelector_SelectionChanged;
    }

    private void ThemeSelector_SelectionChanged(object? sender, SelectionChangedEventArgs e)
    {
        if (Theme.SelectedItem is not ComboBoxItem { Content: string selectedTheme }) return;
        ApplyTheme(selectedTheme);
        SavePreferences(selectedTheme);
    }

    private void ApplyTheme(string? selectedTheme)
    {
        var styles = Application.Current?.Styles;

        if (styles is { Count: > 1 })
        {
            styles.RemoveAt(1);
        }

        if (string.IsNullOrEmpty(selectedTheme))
        {
            selectedTheme = "System";
        }
        
        var url = selectedTheme switch
        {
            "Light" => new Uri("avares://Shinys-Ultimate-Mod-Manager/Themes/LightTheme.axaml"),
            "Dark" => new Uri("avares://Shinys-Ultimate-Mod-Manager/Themes/DarkTheme.axaml"),
            "System" => GetSystemThemeUri(),
            _ => null
        };

        if (url is null) return;
        var theme = new StyleInclude(new Uri("resm:Styles?assembly=Shinys-Ultimate-Mod-Manager"))
        {
            Source = url
        };
        switch (selectedTheme)
        {
            case "System": Theme.SelectedIndex = 0; break;
            case "Dark": Theme.SelectedIndex = 1; break;
            case "Light": Theme.SelectedIndex = 2; break;
        }
        
        styles?.Insert(1, theme);
    }

    private static string GetPreferencesFilePath()
    {
        var folder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
        var appFolder = Path.Combine(folder, "Shinys_Ultimate_Mod_Manager");
        Directory.CreateDirectory(appFolder);
        return Path.Combine(appFolder, "Preferences.json");
    }

    private void SavePreferences(string selectedTheme)
    {
        var prefs = new UserPreferences { Theme = selectedTheme };
        var json = JsonSerializer.Serialize(prefs);
        var path = GetPreferencesFilePath();
        Console.WriteLine($"Saving preferences: {selectedTheme} at {path}");
        File.WriteAllText(GetPreferencesFilePath(), json);
    }

    private string? LoadSavedTheme()
    {
        string path = GetPreferencesFilePath();
        if (File.Exists(path))
        {
            try
            {
                var json = File.ReadAllText(path);
                var prefs = JsonSerializer.Deserialize<UserPreferences>(json);
                Console.WriteLine($"Loaded preferences: {prefs?.Theme}");
                return prefs?.Theme;
            }
            catch (Exception e)
            {
                Console.WriteLine("Failed to load preferences from file: " + e);
            }
        }
        return null;
    }

    private Uri? GetSystemThemeUri()
    {
        string theme = "Dark";

        if (OperatingSystem.IsWindows())
        {
            theme = GetWindowsSystemTheme();
        }
        
        else if (OperatingSystem.IsLinux())
        {
            theme = GetLinuxSystemTheme();
        }
        
        else if (OperatingSystem.IsMacOS())
        {
            theme = GetMacSystemTheme();
        }
        else
        {
            theme = "Dark";
            Console.WriteLine("Failed to get system theme. Defaulting to Dark.");
        }
        
        Console.WriteLine($"Selected theme: {theme}");
        return new Uri($"avares://Shinys-Ultimate-Mod-Manager/Themes/{theme}Theme.axaml");
    }

    private string GetWindowsSystemTheme()
    {
        const string registryKeyPath = @"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize";
        const string valueName = "AppsUseLightTheme";
        
        try
        {
            Console.WriteLine("Getting Windows system theme...");
#pragma warning disable CA1416
            using var key = Microsoft.Win32.Registry.CurrentUser.OpenSubKey(registryKeyPath);
            if (key?.GetValue(valueName) is int value)
#pragma warning restore CA1416
            {
                return value == 0 ? "Dark" : "Light";
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Failed to get Windows System Theme. Defaulting to Dark.\n{e}");
        }
        return "Dark";
    }

    private string GetLinuxSystemTheme()
    {
        try
        {
            Console.WriteLine("Getting Linux system theme...");
            var data = GetLinuxEnvironment();
            string fileName = data.Item1;
            string arguments = data.Item2;
            
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = fileName,
                    Arguments = arguments,
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };

            process.Start();
            string result = process.StandardOutput.ReadToEnd().Trim().ToLower().Replace("\"", "");
            process.WaitForExit();

            if (result.Contains("dark"))
            {
                return "Dark";
            }

            return "Light";
        }
        catch (Exception e)
        {
            Console.WriteLine($"Failed to get Linux theme. Unsupported.\n{e}");
            return "Dark";
        }
    }

    private (string, string) GetLinuxEnvironment()
    {
        string? de = Environment.GetEnvironmentVariable("XDG_CURRENT_DESKTOP");
        
        if (string.IsNullOrEmpty(de))
        {
            Console.WriteLine("No XDG_CURRENT_DESKTOP environment found. Trying with gnome.");
            de = "gnome";
        }
        
        de = de.Split(":", StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.ToLower() ?? "gnome";
        
        Console.WriteLine($"Linux environment: {de}");
        
        return de.ToLower() switch
        {
            "gnome" => ("gsettings", "get org.gnome.desktop.interface gtk-theme"),
            "kde" => ("kwriteconfig5", "--file kwinrc CurrentTheme"),
            "xfce" => ("xfconf-query", "-c xsettings -p /Net/ThemeName"),
            "cinnamon" => ("gsettings", "get org.cinnamon.desktop.wm.preferences theme"),
            "mate" => ("gsettings", "get org.mate.interface gtk-theme"),
            _ => ("gsettings", "get org.gnome.desktop.interface gtk-theme")
        };
    }

    private string GetMacSystemTheme()
    {
        try
        {
            Console.WriteLine("Getting Mac system theme...");
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "defaults",
                    Arguments = "read -g AppleInterfaceStyle",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };

            process.Start();
            string result = process.StandardOutput.ReadToEnd().Trim().ToLower();
            string error = process.StandardError.ReadToEnd().Trim();
            process.WaitForExit();
            
            if (!string.IsNullOrEmpty(error))
                Console.WriteLine($"Failed to get Mac System theme.\n{error}");
            
            if (result.Contains("dark"))
                return "Dark";
            return "Light";

        }
        catch (Exception e)
        {
            Console.WriteLine($"Failed to get Mac system theme.\n{e}");
            return "Dark";
        }
    }
}

public class UserPreferences
{
    public string Theme { get; set; } = "System";
    public string SdCardPath { get; set; } = "";
}