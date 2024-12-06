import boto3
import logging

# Initialize Boto3 client for EC2
ec2 = boto3.client('ec2')

# Setup basic logging
logging.basicConfig(level=logging.INFO)

def terminate_specific_instance(instance_id):
    logging.info(f"Checking and terminating EC2 instance: {instance_id}")
    try:
        # Verify the instance exists and its state
        response = ec2.describe_instances(InstanceIds=[instance_id])
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                current_state = instance['State']['Name']
                logging.info(f"Instance {instance_id} is in state: {current_state}")

                if current_state in ['running', 'stopped']:
                    # Terminate the instance
                    logging.info(f"Terminating instance: {instance_id}")
                    ec2.terminate_instances(InstanceIds=[instance_id])
                    logging.info(f"Instance {instance_id} terminated successfully.")
                else:
                    logging.warning(f"Instance {instance_id} is in state: {current_state}. No action taken.")
    except Exception as e:
        logging.error(f"Error terminating instance {instance_id}: {e}")

if __name__ == "__main__":
    # Replace 'your-instance-id' with the specific instance ID
    specific_instance_id = "i-0e6f9431065eb4675"
    terminate_specific_instance(specific_instance_id)

