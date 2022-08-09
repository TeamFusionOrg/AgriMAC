close all;
clear all;

% This script will simmulate the relative humidity changes inside the
% dehumiditifier
% Simmulation Version 1
% Date : 9th AUG 2022

%% Defining Constants
R = 8.314462618; % specific gas constant
T_Room_1 = 280:15:340; % room temperature
T_Room_2 = T_Room_1 - 15;%298 - 15;
e0 = 0.6113e3; % Saturation Water Vapor pressure at 0C
L = 2264.705e3; % Specific Latent heat of water
mH20 = 18.01528; % molecular mass of water
P_Room_1 = 101.3e3; % Standard Room Pressure at Sea Level
R_vapor = R * 1e3 / mH20; % Gas Constant of water vapor
V_tube = pi * (0.05) * (0.05) * 0.3; % volume of the tube
Alpha_max = 8; % Alpha is the compression ratio. Max value is 8


%% Calculating the relationship between RH1 vs COMPRESSION RATIO
Ps2 = GetSatVaporPressure(T_Room_2);
Ps1 = GetSatVaporPressure(T_Room_1);
RH_Room_1 = 0.1:0.01:1; % Relative Humidity in room before process
compression_ratio = (T_Room_1 ./ T_Room_2)' .* (Ps2 ./ Ps1)' .* (1 ./ RH_Room_1);
% Plot the calcu
figure
plot(RH_Room_1 * 100, compression_ratio);
labels = {};
for temp_index = 1:length(T_Room_1)
    labels{end + 1} = "Room Temp: " + num2str(T_Room_1(temp_index)) + " K";
end
title ("Starting RH vs Compression Ratio");
xlabel("Starting RH (%)");
ylabel("Compression Ratio");
legend(labels,'Location','northeast')
grid on;

%% Calulation of the water condense

mass_ratio = Alpha_max ./ compression_ratio;

figure
plot(RH_Room_1 * 100, mass_ratio);
title ("Starting RH vs Mass Condensig Ratio");
xlabel("Starting RH (%)");
ylabel("Mass Condensing");
legend(labels,'Location','northeast')
grid on;

Start_Mass = RH_Room_1 .* ((Ps1 .* V_tube) ./ (R_vapor .* T_Room_1))';
mass_condence = Start_Mass .* (1 - 1 ./ mass_ratio);

figure
plot(RH_Room_1 * 100, mass_condence * 1e6);
title ("Starting RH vs Condensing Water Mass per stroke");
xlabel("Starting RH (%)");
ylabel("Water Mass (mg)");
legend(labels,'Location','northeast')
grid on;

%% Calculating Finishing Humidity

mass_left = Start_Mass ./ mass_ratio;
RH2 = (T_Room_1' .* (R_vapor * mass_left)) ./ (Ps1' * V_tube);

figure
plot(RH_Room_1 * 100, RH2 * 100);
title ("Starting RH vs Finishing RH");
xlabel("Starting RH (%)");
ylabel("Finishing RH (%)");
legend(labels,'Location','northeast')
grid on;

%% Calculating the Finishing Humidity with the temperature

Temps = 280:0.1:320;
RH2_ = (GetSatVaporPressure(Temps - 15) ./ GetSatVaporPressure(Temps)) .* (Temps ./ (Temps-15)) .* (1/8);

figure
plot(Temps - 273.15, RH2_ * 100);
title ("Room Temperature vs Finishing RH");
xlabel("Room Temperature (Celcius)");
ylabel("Finishing RH (%)");
grid on;