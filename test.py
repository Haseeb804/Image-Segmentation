import torch
import torch.nn as nn
import torchvision.transforms.functional as tf

class DoubleConv(nn.modules):
    def __init__ (self, in_channels, out_channels):
        super(DoubleConv, self).__init__ ()
        self.conv == nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3,1,1, bias = False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, 3,1,1, bias = False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )
    def forward(self, x):
        return self.conv(x)

#creating a unet architecture
class UNET(nn.modules):
    def __init__ (self, in_channels = 3, out_channels = 1, features = [64, 128, 256, 512]  
    ):
        super(UNET,self.__init__())
        self.ups = nn.ModuleList()
        self.downs = nn.ModuleList()
        self.pool = nn.MaxPool2d(kernel_size = 2, stride = 2)
        
        # down part of UNet
        for feature in features:
            self.downs.append(DoubleConv(in_channels, features))
            in_channels = features

        #up part of UNet
        for feature in reversed(features):
            self.ups.append(
                nn.ConvTranspose2d(
                    features*2, feature, kernel_size = 2, stride = 2
                )
            )
            self.ups.append(DoubleConv(features*2, feature))

        self.bottleneck = DoubleConv(features[-1], features[-1]*2)
        self.final_conv = nn.Conv2d(features[0], out_channels, kernel_size = 1)
     