# class MyAugmentation(nn.Module):
#   def __init__(self):
#     super(MyAugmentation, self).__init__()
#     # we define and cache our operators as class members
#     # self.k1 = K.augmentation.ColorJitter(0.15, 0.25, 0.25, 0.25)
#     self.k1 = K.augmentation.RandomCrop((256,256))
#     self.k2 = K.augmentation.RandomAffine([-45., 45.], [0., 0.15], [0.5, 1.5], [0., 0.15])
  
#   def forward(self, img: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
#     # 1. apply color only in image
#     # 2. apply geometric tranform
#     img_out = self.k2(self.k1(img))

#     # 3. infer geometry params to mask
#     # TODO: this will change in future so that no need to infer params
#     mask = self.k1(mask, self.k1._params)
#     mask_out = self.k2(mask, self.k2._params)

#     return img_out, mask_out

# aug = MyAugmentation()

# img_aug, labels_aug = aug(img, target)
# img_aug.shape, labels_aug.shape

# img_out = torch.cat([img_aug.int(), labels_aug.int()], dim=-1)
# plt.imshow(K.tensor_to_image(img_out))
# plt.axis('off')

# img_out = torch.cat([img.int(), target.int()], dim=-1)
# plt.imshow(K.tensor_to_image(img_out))
# plt.axis('off')