export IMAGE_NAME="obstacle_tower_challenge"

aicrowd-repo2docker --no-run \
  --image-name ${IMAGE_NAME} \
  --user-name aicrowd \
  --debug .
