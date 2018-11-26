export IMAGE_NAME="obstacle_tower_challenge"

crowdai-repo2docker --no-run \
  --user-id 1001 \
  --user-name crowdai \
  --image-name ${IMAGE_NAME} \
  --debug .
