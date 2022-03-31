package commands

import (
	"context"

	"github.com/spf13/cobra"
)

var (
	version  = "unknown"
	LogLevel string
)

func NewRootCmd(cancel context.CancelFunc) *cobra.Command {
	cmd := &cobra.Command{
		Use:     "flet",
		Short:   "Flet",
		Version: version,
		PersistentPreRun: func(cmd *cobra.Command, args []string) {
			configLogging()
		},
	}

	cmd.SetVersionTemplate("{{.Version}}")

	cmd.PersistentFlags().StringVarP(&LogLevel, "log-level", "l", "info", "verbosity level for logs")

	cmd.AddCommand(
		newServerCommand(cancel),
	)

	return cmd
}
