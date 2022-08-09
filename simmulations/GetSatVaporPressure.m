function [SatVaporP] = GetSatVaporPressure(Temp)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
R = 8.314462618; % specific gas constant
mH20 = 18.01528; % molecular mass of water
R_vapor = R * 1e3 / mH20;
L = 2264.705e3; % Specific Latent heat of water
e0 = 0.6113e3; % Saturation Water Vapor pressure at 0C

SatVaporP = e0 * exp((L/R_vapor) *(1./273.15 - 1./Temp));
end

