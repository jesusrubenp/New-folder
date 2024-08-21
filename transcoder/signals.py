from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
import subprocess
import os

@receiver(post_save, sender=Video)
def transcode_video(sender, instance, created, **kwargs):
    if created:  # Solo transcodificar cuando el video es creado por primera vez
        input_file = instance.original_file.path
        output_file = instance.original_file.path.replace('originals', 'transcoded').replace('.mp4', '_transcoded.mp4')
        
        # Comando FFmpeg para transcodificar
        command = [
            'ffmpeg',
            '-i', input_file,  # Archivo de entrada
            '-vcodec', 'libx264',  # Codec de video
            '-acodec', 'aac',  # Codec de audio
            output_file  # Archivo de salida
        ]
        
        subprocess.run(command, check=True)
        
        # Actualizar la ruta del archivo transcodificado en el modelo
        instance.transcoded_file.name = output_file.split('/')[-1]
        instance.save()
